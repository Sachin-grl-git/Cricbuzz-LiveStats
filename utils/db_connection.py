from sqlalchemy import create_engine
import json, os

def get_db_connection():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.json")
    with open(config_path) as f:
        config = json.load(f)

    db = config["DB"]
    db_url = f"{db['DB_TYPE']}://{db['USER']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['DB_NAME']}"

    engine = create_engine(db_url)
    return engine
