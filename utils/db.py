# utils/db.py
from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from urllib.parse import quote_plus

# 1) load_dotenv(find_dotenv()) will search up from cwd until it finds your .env
load_dotenv(find_dotenv())

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "music_test")

ENCODED_PASS = quote_plus(DB_PASS)
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{ENCODED_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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
