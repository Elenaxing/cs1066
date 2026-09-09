# EDGAR financial trends dashboard development
_Exported on 6/12/2026 at 13:12:43 EDT from Cursor (3.3.16)_

---

**User**

Build a Python Streamlit application called “EDGAR Financial Trends Dashboard.”

Goal:
Allow a user to search for a publicly traded company, choose a fiscal-year range,
and generate three vertically stacked interactive line charts:

1. Annual revenue versus fiscal year
2. Annual net income versus fiscal year
3. Total assets versus fiscal year

Use only official SEC EDGAR data.

Technology:
- Python
- Streamlit
- Plotly
- Pandas
- Requests
- RapidFuzz
- Pytest

Do not use a paid or third-party financial API.
The official SEC data API requires no API key.

SEC resources:
- Company lookup:
  https://www.sec.gov/files/company_tickers.json
- Company Facts:
  https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
- Submissions:
  https://data.sec.gov/submissions/CIK##########.json

Every SEC request must contain a descriptive User-Agent read from the
SEC_USER_AGENT environment variable. Add timeouts, retries, exponential backoff,
caching, and a rate limiter no higher than 5 requests per second.

Create this structure:

edgar-dashboard/
  app.py
  requirements.txt
  README.md
  .env.example
  src/
    __init__.py
    models.py
    sec_client.py
    company_search.py
    facts_extractor.py
    charts.py
    insights.py
  tests/
    fixtures/
    test_company_search.py
    test_facts_extractor.py
    test_charts.py

Company search:
- Prioritize exact ticker matches.
- Then match company-name prefixes, substrings, and fuzzy results.
- Show company name, ticker, and ten-digit CIK.
- Never silently choose an ambiguous company.

Metric concepts:

US GAAP revenue priority:
1. RevenueFromContractWithCustomerExcludingAssessedTax
2. Revenues
3. SalesRevenueNet

US GAAP net income:
1. NetIncomeLoss

US GAAP assets:
1. Assets

IFRS:
- Revenue
- ProfitLoss
- Assets

Annual forms:
- 10-K
- 10-K/A
- 20-F
- 20-F/A
- 40-F
- 40-F/A

Extraction rules:
- Use standardized Company Facts XBRL data only.
- Match each fact to an annual filing by accession number.
- Require fp == FY when available.
- Match the fact period end to the filing reportDate.
- Revenue and net income must be full-year duration facts.
- Assets must be an instantaneous period-end fact.
- Preserve the original unit and currency.
- Do not convert currencies.
- Do not interpolate.
- Do not fill missing values with zero.
- Do not substitute related but different financial concepts.
- If equally valid facts conflict, omit the point and show a warning.
- Prefer a valid later amendment for the same report date.
- Store point-level provenance.

Create a FactPoint data model containing:
metric, fiscal_year, raw value, unit, taxonomy, concept, period_start,
period_end, form, accession number, filed date, and source URL.

UI:
- Company search field
- Company selector
- Start year
- End year
- “All available years” option
- Generate Dashboard button
- Clear error and loading states

Charts:
- Revenue, Net Income, and Assets, stacked vertically
- Plotly lines plus markers
- connectgaps=False
- Exact-value hover tooltips
- Wheel zoom enabled
- Pan and reset controls
- X-axis range slider
- Fiscal year tick interval of one
- Full-width responsive layout

Hover data:
- Fiscal year
- Exact raw value
- Unit
- Period start/end
- Form
- Filing date
- Taxonomy and concept

Below the charts, add an expandable “SEC source data” table and a CSV download.
Every plotted point must appear in this table and must link to its original SEC filing.

Add a deterministic insights section only. It may calculate percent changes,
year-over-year changes, maxima, minima, and missing-year counts. Do not use an
LLM and do not make causal or investment claims.

Write tests using local SEC response fixtures. Tests must cover quarterly-data
rejection, annual extraction, alternate revenue concepts, amendments, missing
years, negative income, duplicate facts, year filtering, and source provenance.

Create a README with setup instructions, environment-variable instructions,
local run commands, testing commands, data limitations, and SEC fair-access
requirements.

Implement the application incrementally. First create the file structure and
data models, then the SEC client, then extraction tests, then the Streamlit UI.
Run the test suite after each major stage.
