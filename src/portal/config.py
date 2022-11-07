import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432
    password = os.environ.get("DB_PASSWORD", "abc123")
    user, db_name = "oskar", "rating_portal"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 8000 if host == "localhost" else 80
    return f"http://{host}:{port}"


get_session = sessionmaker(bind=create_engine(get_postgres_uri()))
