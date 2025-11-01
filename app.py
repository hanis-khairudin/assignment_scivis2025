import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Learning Tech Insights", page_icon="📚", layout="wide")

# Load data from GitHub
url = "https://raw.githubusercontent.com/hanis-khairudin/assignment_scivis2025/refs/heads/main/FULLTIME%20STUDENT%20USING%20SOCIAL%20MEDIA.csv"
fulltime_students_df = pd.read_csv(url)

# Sidebar navigation
st.sidebar.title("📂 Objectives")
page = st.sidebar.radio("Select Objective", [
    "Objective 1",
    "Objective 2",
    "Objective 3"
])

st.title("📊 Analysis of Students’ Intention Toward Social Media & Emerging Tech")
