import requests
import json
import os

# Load config
config_path = os.path.join("config", "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

def fetch_live_matches():
    url = f"https://{config['API']['CRICBUZZ_RAPIDAPI_HOST']}/matches/v1/live"
    headers = {
        "x-rapidapi-host": config["API"]["CRICBUZZ_RAPIDAPI_HOST"],
        "x-rapidapi-key": config["API"]["CRICBUZZ_RAPIDAPI_KEY"]
    }
    response = requests.get(url, headers=headers)
    return response.json()

# ✅ New function for upcoming matches
def fetch_upcoming_matches():
    url = f"https://{config['API']['CRICBUZZ_RAPIDAPI_HOST']}/matches/v1/upcoming"
    headers = {
        "x-rapidapi-host": config["API"]["CRICBUZZ_RAPIDAPI_HOST"],
        "x-rapidapi-key": config["API"]["CRICBUZZ_RAPIDAPI_KEY"]
    }
    response = requests.get(url, headers=headers)
    return response.json()
