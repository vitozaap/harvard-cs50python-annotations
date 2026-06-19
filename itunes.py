import requests
from sys import argv, exit
import json


def main():
    if len(argv) != 3:
        exit("Maybe you're missing some arguments")
    # Requesting using get method and getting the "result" key
    response = requests.get(
        f"https://itunes.apple.com/search?entity=song&limit={argv[2]}&term={argv[1]}"
    ).json()["results"]
    # Returning only the key "results" values
    # dumps = dump string
    json.dumps(response, indent=2)
    for track in response:
        print(f"{track['trackName']}")


main()
