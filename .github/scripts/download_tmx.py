#! /usr/bin/env python3

import os
import requests


def main():
    # Get the list of Pontoon locales
    url = "https://pontoon.mozilla.org/api/v2/locales/?fields=code"
    try:
        page = 1
        locales = []
        while url:
            print(f"Reading locales from Pontoon (page {page})")
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            page_locales = [locale["code"] for locale in data.get("results", [])]
            locales.extend(page_locales)

            # Get the next page URL
            url = data.get("next")
            page += 1
        locales.sort()
    except requests.RequestException as e:
        print(e)

    # Get root path
    root_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    )

    for locale in locales:
        # Create locale folder if missing
        locale_path = os.path.join(root_path, locale)
        if not os.path.isdir(locale_path):
            os.mkdir(locale_path)

        print(f"Downloading TMX for {locale}")
        try:
            response = requests.get(
                f"https://pontoon.mozilla.org/translation-memory/{locale}.all-projects.tmx"
            )

            with open(os.path.join(locale_path, f"{locale}_pontoon.tmx"), "wb") as f:
                f.write(response.content)
        except requests.RequestException as e:
            print(e)


if __name__ == "__main__":
    main()
