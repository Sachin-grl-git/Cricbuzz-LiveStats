from sqlalchemy import create_engine
import json, os

def get_db_connection():
    # Load config
    config_path = os.path.join("config", "config.json")
    with open(config_path, "r") as f:
        cfg = json.load(f)

    db_url = cfg["DB"]["DB_TYPE"]
    engine = create_engine(db_url, echo=False)
    return engine
