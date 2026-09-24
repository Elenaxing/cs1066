"""Run with: python -m streamlit run m04/financial_webapp.py."""

from datetime import date
from math import isfinite

import matplotlib

# Render plots in the webpage without opening desktop plot windows.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import requests
import streamlit as st


# The SEC requires a User-Agent identifying the requester.
USER_AGENT = "UniversityStudent your.email@harvard.edu"


def extract_annual_values(data, tags, instant=False):
    """Return annual USD facts, keyed by period-end year.

    Tags are listed in preference order, with older tags filling missing years.
    Within a tag, use the latest filing for each year-end date. Full-year
    durations allow 52/53-week calendars but exclude quarters and year-to-date
    figures. Assets are an instant balance, so they have no start date.
    """
    facts = data.get("facts")
    if not isinstance(facts, dict):
        return {}
    facts = facts.get("us-gaap")
    if not isinstance(facts, dict):
        return {}
    annual_values = {}

    for tag in tags:
        tag_values = {}
        concept = facts.get(tag)
        if not isinstance(concept, dict):
            continue
        units = concept.get("units")
        if not isinstance(units, dict):
            continue
        records = units.get("USD")
        if not isinstance(records, list):
            continue
        for fact in records:
            if not isinstance(fact, dict):
                continue
            if fact.get("form") not in ("10-K", "10-K/A", "20-F", "20-F/A"):
                continue
            if fact.get("fp") != "FY" or not isinstance(fact.get("val"), (int, float)):
                continue
            # Skip unusable records while preserving other available years.
            if isinstance(fact["val"], bool) or not isfinite(fact["val"]):
                continue
            if not isinstance(fact.get("filed", ""), str):
                continue

            try:
                end = date.fromisoformat(fact["end"])
                if not instant:
                    start = date.fromisoformat(fact["start"])
                    if not 330 <= (end - start).days <= 400:
                        continue
                elif "start" in fact:
                    continue
            except (KeyError, TypeError, ValueError):
                continue

            # A filing's fy refers to the report, including its comparative
            # figures. The fact's end date identifies the value's actual year.
            year = end.year
            previous = tag_values.get(year)
            rank = (fact["end"], fact.get("filed", ""))
            if previous is None or rank > (previous["end"], previous.get("filed", "")):
                tag_values[year] = fact

        for year, fact in tag_values.items():
            if year not in annual_values:
                annual_values[year] = {**fact, "tag": tag}

    return dict(sorted(annual_values.items()))


def print_annual_financials(data):
    """Print and return up to the latest 10 years per measure, oldest first."""
    measures = {
        "Revenue": [
            "RevenueFromContractWithCustomerExcludingAssessedTax",
            "RevenueFromContractWithCustomerIncludingAssessedTax",
            "Revenues",
            "SalesRevenueNet",
        ],
        "Net income": ["NetIncomeLoss", "ProfitLoss"],
        "Assets": ["Assets"],
    }

    cleaned_data = {}
    for measure, tags in measures.items():
        values = extract_annual_values(data, tags, instant=measure == "Assets")
        # Select each measure independently; shorter histories keep every year.
        values = dict(sorted(values.items())[-10:])
        cleaned_data[measure] = values
        print(f"\n{measure} (USD; year is the period-end year):")
        if not values:
            print("No annual USD data found for the supported US-GAAP tags.")
            continue
        for year, fact in values.items():
            print(f"{year}: {fact['val']:,.2f} (ended {fact['end']}; {fact['tag']})")

    return cleaned_data


def plot_annual_financials(company_name, cleaned_data):
    """Stack the existing plots vertically in the webpage."""
    colors = {"Revenue": "tab:blue", "Net income": "tab:green", "Assets": "tab:purple"}
    for measure, values in cleaned_data.items():
        if not values:
            st.warning(
                f"{measure}: No usable annual USD data were found in the SEC response. "
                "This plot is unavailable. Other available measures are still shown."
            )
            continue

        years = sorted(values)
        amounts = [values[year]["val"] for year in years]
        fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
        ax.plot(years, amounts, marker="o", linewidth=2, color=colors[measure])
        ax.set_title(f"{company_name}\n{measure} over time ({years[0]}–{years[-1]})")
        ax.set_xlabel("Year (period-end year)")
        ax.set_ylabel(f"{measure} (USD)")
        ax.set_xticks(years)
        ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
        ax.grid(True, alpha=0.3)
        if min(amounts) < 0:
            ax.axhline(0, color="gray", linewidth=0.8)

        st.pyplot(fig)
        plt.close(fig)


def main():
    st.set_page_config(page_title="Company financials", layout="centered")
    st.title("Company financials")
    st.write("View annual revenue, net income, and assets for a company.")
    with st.form("company_lookup"):
        cik = st.text_input(
            "Company's 10-digit CIK number",
            placeholder="0000002488",
            help="Include all leading zeros. Example: AMD is 0000002488.",
        )
        submitted = st.form_submit_button("Show financials")

    if not submitted:
        return

    # Keep the CIK as a string so its leading zeros are preserved.
    cik = cik.strip()
    if not cik:
        st.error("Please enter a company's 10-digit CIK number, such as 0000002488 for AMD.")
        return
    if len(cik) != 10 or not cik.isascii() or not cik.isdigit():
        st.error("Please enter exactly 10 digits, including any leading zeros (for example, 0000002488).")
        return

    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    headers = {"User-Agent": USER_AGENT}

    try:
        with st.spinner("Retrieving company facts…"):
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
    except (requests.exceptions.JSONDecodeError, UnicodeDecodeError):
        st.error("The SEC returned an unreadable response. Please try again later.")
        return
    except requests.exceptions.Timeout:
        st.error("The SEC request timed out. Please try again in a moment.")
        return
    except requests.exceptions.HTTPError as error:
        status = error.response.status_code if error.response is not None else None
        if status == 404:
            st.error("No SEC company facts were found for this CIK. Check the number or try another company.")
        elif status == 403:
            st.error("The SEC denied access to the request. Please wait and try again later.")
        elif status == 429:
            st.error("The SEC is limiting requests. Please wait a few minutes before trying again.")
        elif status is not None and status >= 500:
            st.error("The SEC service is temporarily unavailable. Please try again later.")
        else:
            st.error("The SEC could not complete the request. Check the CIK and try again later.")
        return
    except (requests.exceptions.RequestException, OSError):
        st.error("Could not connect to the SEC. Check your internet connection and try again.")
        return

    if (
        not isinstance(data, dict)
        or not isinstance(data.get("entityName"), str)
        or not data["entityName"].strip()
    ):
        st.error("The SEC returned incomplete company data without a valid company name. Please try again later.")
        return

    st.header(data["entityName"])
    st.success("Company facts data were retrieved successfully.")
    st.caption("Latest 10 available years for each measure, shown oldest to newest. All values are in USD.")
    cleaned_data = print_annual_financials(data)
    plot_annual_financials(data["entityName"], cleaned_data)


if __name__ == "__main__":
    main()
