import json
import requests

FEED_URL = "https://httpbin.org/json"


def fetch_feed(url=FEED_URL):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def count_keys(payload):
    return len(payload.keys())


def summarise(payload):
    return f"Feed returned {count_keys(payload)} top-level keys"


if __name__ == "__main__":
    data = fetch_feed()
    print(summarise(data))
