import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os

# ────────────────────── DATABASE CONNECTION ──────────────────────
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "Sathwickkiran@12")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "music_test")
ENCODED_PASS = quote_plus(DB_PASS)
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{ENCODED_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# ────────────────────── PAGE CONFIG ──────────────────────
st.set_page_config(
    page_title="🎵 Music Store Dashboard",
    page_icon="🎶",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ────────────────────── HELPERS ──────────────────────
def run_query(q, return_df=True):
    with engine.connect() as conn:
        result = conn.execute(text(q))
        if return_df:
            return pd.DataFrame(result.fetchall(), columns=result.keys())

# ────────────────────── SIDEBAR ──────────────────────
st.sidebar.markdown("<h1 style='color:#ffffff;'>🎧 Music Store</h1>", unsafe_allow_html=True)
section = st.sidebar.radio("Navigation", [
    "🏠 Home",
    "🎶 Tracks",
    "👥 Customers",
    "📀 Genres & Media",
    "💸 Sales",
    "🛠️ Admin"
])

# ────────────────────── HOMEPAGE ──────────────────────
if section == "🏠 Home":
    st.markdown("""
        <style>
        .hero {
            text-align: center;
            padding: 3rem 2rem 1rem;
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            border-radius: 10px;
        }
        .hero h1 {
            font-size: 3rem;
            font-weight: 800;
        }
        .hero p {
            font-size: 1.2rem;
            font-weight: 300;
        }
        .features {
            display: flex;
            justify-content: space-around;
            gap: 2rem;
            margin-top: 2rem;
            flex-wrap: wrap;
        }
        .feature-card {
            flex: 1;
            min-width: 250px;
            background-color: #f5f5f5;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        .feature-card h3 {
            margin-top: 0.5rem;
            font-size: 1.3rem;
        }
        .feature-card p {
            font-size: 0.95rem;
            line-height: 1.5;
        }
        .cta {
            text-align: center;
            margin: 3rem 0;
        }
        .cta a {
            font-size: 1.1rem;
            background-color: #2563eb;
            color: white;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 8px;
            transition: 0.3s;
        }
        .cta a:hover {
            background-color: #1d4ed8;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='hero'>
            <h1>🎵 Welcome to the Music Store Dashboard</h1>
            <p>Browse tracks, explore customers and invoices, analyze pricing — all in one place.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='features'>
            <div class='feature-card'>
                <h3>🎼 Track Explorer</h3>
                <p>Browse our full catalog of 3,500+ tracks. Filter by name, duration, or genre to find the right sound.</p>
            </div>
            <div class='feature-card'>
                <h3>🧾 Customer Billing</h3>
                <p>Analyze customer billing data, view locations, and manage user records through a simplified view.</p>
            </div>
            <div class='feature-card'>
                <h3>📊 Insights & Reports</h3>
                <p>Visualize top spenders, monitor total invoices, and break down genre/media type distributions.</p>
            </div>
            <div class='feature-card'>
                <h3>🛠️ Admin Controls</h3>
                <p>Add or remove customer data directly from the dashboard using secure operations.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='cta'>
            <a href="/" target="_self">🎧 Explore Tracks Now</a>
        </div>
    """, unsafe_allow_html=True)

# You can keep the other sections (Tracks, Customers, etc.) the same.
# Just plug this in place of your "🏠 Home" section and you're set!
