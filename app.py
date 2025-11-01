import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Full-Time Student Social Media Usage", page_icon="📊", layout="wide")

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="🧠🔬 Scientific Visualization")

st.header("🧠 Scientific Visualization 🔬", divider="gray")
st.write("Tutorial Scientific Visualization JIE42403 📊💡")
st.write("Dataset 'Student Survey' by Razib Mustafiz from Kaggle")

# --- 3. LOAD DATA FROM GITHUB ---
url = "https://raw.githubusercontent.com/hanis-khairudin/assignment_scivis2025/refs/heads/main/FULLTIME%20STUDENT%20USING%20SOCIAL%20MEDIA.csv"
    return pd.read_csv(url)

try:
    students_df = pd.read_csv(url)
    st.dataframe(arts_df.head())
