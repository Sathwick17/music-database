# utils/db.py
# from sqlalchemy import create_engine, text
# import pandas as pd
# import os
# from dotenv import load_dotenv, find_dotenv
# from urllib.parse import quote_plus

# from sqlalchemy import create_engine, text
# import pandas as pd
# import os
# from dotenv import load_dotenv
# from urllib.parse import quote_plus

# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASS = quote_plus(os.getenv("DB_PASS"))
# DB_NAME = os.getenv("DB_NAME")

# # ⚡ Force host=/tmp for Unix socket connection
# DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@/{DB_NAME}?host=/tmp"

# engine = create_engine(DATABASE_URL)

# def load_query(query_filename):
#     # 2) point to your actual folder name
#     path = os.path.join("SQL", query_filename)
#     with open(path, "r") as f:
#         return f.read()

# def run_query(query_filename):
#     query = load_query(query_filename)
#     with engine.connect() as conn:
#         return pd.read_sql_query(text(query), conn)


# --- utils/db.py ---
import streamlit as st
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Build database connection details
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.OperationalError as e:
        st.error(f"❌ Could not connect to the PostgreSQL database.\n\nError details:\n{e}")
        return None

# Function to run a query from a file
def run_query_from_file(filename):
    sql_folder = "SQL"  # Folder where your SQL files are stored
    filepath = os.path.join(sql_folder, filename)
    with open(filepath, "r") as file:
        query = file.read()
    return run_query_direct(query)

# Function to run a direct query text
def run_query_direct(query):
    conn = get_connection()
    if conn is None:
        return []
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except Exception as e:
        st.error(f"❌ Query failed:\n\n{e}")
        if conn:
            conn.close()
        return []

# Function to load a query text from file for display
def load_query(filename):
    sql_folder = "SQL"
    filepath = os.path.join(sql_folder, filename)
    with open(filepath, "r") as file:
        query = file.read()
    return query
