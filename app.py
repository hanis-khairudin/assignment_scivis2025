import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Full-Time Student Social Media Usage", page_icon="📊", layout="wide")

# Data loading
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/hanis-khairudin/assignment_scivis2025/refs/heads/main/FULLTIME%20STUDENT%20USING%20SOCIAL%20MEDIA.csv"
    return pd.read_csv(url)

df = load_data()

# Sidebar nav
page = st.sidebar.radio(
    "Navigate",
    ["Demographics & E-learning", "Social Media Platforms", "Frequency of Visits"]
)

st.title("📚 Full-Time Student Social Media Usage Dashboard")
