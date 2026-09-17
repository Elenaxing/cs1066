### m03/dog_requests.py
import requests


def get_wikipedia_intro(title: str) -> str:
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "exintro": 1,
        "titles": title,
        "format": "json",
    }
    headers={"User-Agent": "Harvard CS1066 bot"}

    response = requests.get(api_url, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        if page.get("extract"):
            return page["extract"].strip()

    raise ValueError(f"Could not find an intro paragraph for '{title}'.")


if __name__ == "__main__":
    intro = get_wikipedia_intro("Dog")
    print(intro)
