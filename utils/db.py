# utils/db.py
# from sqlalchemy import create_engine, text
# import pandas as pd
# import os
# from dotenv import load_dotenv, find_dotenv
# from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = quote_plus(os.getenv("DB_PASS"))
DB_NAME = os.getenv("DB_NAME")

# ⚡ Force host=/tmp for Unix socket connection
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@/{DB_NAME}?host=/tmp"

engine = create_engine(DATABASE_URL)

def load_query(query_filename):
    # 2) point to your actual folder name
    path = os.path.join("SQL", query_filename)
    with open(path, "r") as f:
        return f.read()

def run_query(query_filename):
    query = load_query(query_filename)
    with engine.connect() as conn:
        return pd.read_sql_query(text(query), conn)
