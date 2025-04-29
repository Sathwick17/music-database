# app.py

# import streamlit as st
# from utils.db import run_query, load_query
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # App Title and Config
# st.set_page_config(
#     page_title="🎵 Music Store Dashboard",
#     page_icon="🎶",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# st.title("🎵 Music Store Database Explorer (Local PostgreSQL)")

# # List of available queries
# SQL = {
#     "👥 Customers and Their Cities": "Customers_and_their_cities.sql",
#     "🌎 Most Diverse Customers Based on Genre": "most_diverse_customers_based_on_genre.sql",
#     "🎵 Number of Tracks per Genre": "number_of_tracks_per_genre.sql",
#     "⏳ Top 5 Longest Tracks": "top_5_longest_tracks.sql",
#     "💰 Top Artists by Revenue Generated": "top_artists_by_revenue_generated.sql"
# }

# # Dropdown menu
# selected_query = st.selectbox("📄 Select a SQL Query to Explore", list(SQL.keys()))

# try:
#     # Load and run the selected query
#     df = run_query(SQL[selected_query])

#     st.subheader("🧹 SQL Query Used")
#     query_text = load_query(SQL[selected_query])
#     st.code(query_text, language="sql")

#     st.subheader("📊 Query Results")
#     st.dataframe(df)

# except Exception as e:
#     st.error(f"❌ Failed to execute query: {e}")


# --- app.py ---

import streamlit as st
from utils.db import run_query_from_file, run_query_direct, load_query

# App title
st.title("🎵 Music Store Database Explorer (Local PostgreSQL)")

# List of available queries
SQL = {
    "👥 Customers and Their Cities": "Customers_and_their_cities.sql",
    "🌎 Most Diverse Customers Based on Genre": "most_diverse_customers_based_on_genre.sql",
    "🎵 Number of Tracks per Genre": "number_of_tracks_per_genre.sql",
    "⏳ Top 5 Longest Tracks": "top_5_longest_tracks.sql",
    "💰 Top Artists by Revenue Generated": "top_artists_by_revenue_generated.sql"
}

# --- Dropdown menu for pre-defined queries ---
st.header("Select a Predefined Query")
selected_query = st.selectbox("📄 Choose a Query", list(SQL.keys()))

try:
    df = run_query_from_file(SQL[selected_query])

    st.subheader("🧹 SQL Query Used")
    query_text = load_query(SQL[selected_query])
    st.code(query_text, language="sql")

    st.subheader("📊 Query Results")
    st.dataframe(df)

except Exception as e:
    st.error(f"❌ Failed to execute pre-defined query: {e}")

# --- Custom query execution ---
st.header("Write Your Own SQL Query")
custom_query = st.text_area("✏️ Enter your SQL query below:", height=200)

if st.button("🚀 Run Custom Query"):
    if custom_query.strip() == "":
        st.warning("⚠️ Please enter a SQL query.")
    else:
        try:
            df_custom = run_query_direct(custom_query)
            if df_custom:
                st.success("✅ Query executed successfully!")
                st.dataframe(df_custom)
            else:
                st.info("ℹ️ Query executed but returned no results.")
        except Exception as e:
            st.error(f"❌ Failed to execute custom query: {e}")
