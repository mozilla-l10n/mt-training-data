#! /usr/bin/env python3

import json
import os
import requests
import sys
from urllib.request import urlopen


def main():
    # Get the list of Pontoon locales
    try:
        url = "https://pontoon.mozilla.org/graphql?query={locales{code}}"
        print("Reading locales in Pontoon")
        response = urlopen(url)
        json_data = json.load(response)
        locales = [l["code"] for l in json_data["data"]["locales"]]
        locales.sort()
    except Exception as e:
        sys.exit(e)

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
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
