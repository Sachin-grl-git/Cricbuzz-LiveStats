import requests, json, os

def fetch_live_matches():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")
    with open(config_path) as f:
        config = json.load(f)

    url = f"https://{config['API']['CRICBUZZ_RAPIDAPI_HOST']}/matches/v1/live"
    headers = {
        "x-rapidapi-key": config['API']['CRICBUZZ_RAPIDAPI_KEY'],
        "x-rapidapi-host": config['API']['CRICBUZZ_RAPIDAPI_HOST']
    }

    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {}
