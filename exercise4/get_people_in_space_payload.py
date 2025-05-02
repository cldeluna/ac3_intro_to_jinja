#!/usr/bin/python -tt
# Project: ac3_intro_to_jinja
# Filename: get_people_in_space_payload.py
# claudiadeluna
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "5/2/25"
__copyright__ = "Copyright (c) 2023 Claudia"
__license__ = "Python"


import httpx
import json


def fetch_and_save_people_in_space(filename="people_in_space.json"):
    url = "http://api.open-notify.org/astros.json"
    """
    Fetches the list of people in space from the Open Notify API and saves the response as a JSON file.

    :param filename: The name of the file to save the data to. Defaults to "people_in_space.json".
    :return: None
    """
    try:
        response = httpx.get(url)
        response.raise_for_status()
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
        people = data.get("people", [])
        print(f"There are {len(people)} people in space:")
        for person in people:
            print(f"- {person['name']} on {person['craft']}")
    except httpx.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    fetch_and_save_people_in_space()


# Standard call to the main() function.
if __name__ == '__main__':
    main()
