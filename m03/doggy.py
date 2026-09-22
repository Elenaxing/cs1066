### m03/doggy.py
import os
import sys

import requests


API_URL = "https://api.thedogapi.com/v1/images/search"
SECRET_APIKEY = "CS1066_THEDOGAPIKEY"
OUTPUT_FILE = "random_dog.jpg"


def get_api_key() -> str:
    return os.environ.get(SECRET_APIKEY, "YOUR_API_KEY_HERE")


def download_random_dog_image(api_key: str) -> str:
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(API_URL, headers=headers, timeout=20)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch dog image: {exc}") from exc

    if not payload:
        raise RuntimeError("The API returned no image data.")

    image_url = payload[0].get("url")
    if not image_url:
        raise RuntimeError("The API response did not include an image URL.")

    try:
        image_response = requests.get(image_url, timeout=20)
        image_response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to download dog image: {exc}") from exc

    with open(OUTPUT_FILE, "wb") as out_file:
        out_file.write(image_response.content)

    return OUTPUT_FILE


if __name__ == "__main__":
    api_key = get_api_key()
    if api_key == "YOUR_API_KEY_HERE":
        print(f"Set the {SECRET_APIKEY} environment variable before running this script.")
        sys.exit(1)

    try:
        saved_file = download_random_dog_image(api_key)
        print(f"Saved image to {saved_file}")
    except RuntimeError as exc:
        print(exc)
        sys.exit(1)
