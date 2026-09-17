### m03/dog_intro.py
import json
import urllib.parse
import urllib.request


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

    query_string = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{api_url}?{query_string}",
        headers=headers,
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.load(response)

    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        if page.get("extract"):
            return page["extract"].strip()

    raise ValueError(f"Could not find an intro paragraph for '{title}'.")


if __name__ == "__main__":
    intro = get_wikipedia_intro("Dog")
    print(intro)
