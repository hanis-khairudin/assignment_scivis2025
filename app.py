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

st.write(fulltime_students_df.head())

# ========== PAGE 2: Academic Status vs E-Learning ==========
elif page == "Objective 1":
    st.subheader("🎓 Academic Status vs E-learning Involvement")

    grouped_data = df.groupby(
        ["AcademicStatus", "Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore"]
    ).size().reset_index(name="Count")

    fig = px.bar(
        grouped_data,
        x="AcademicStatus",
        y="Count",
        color="Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore",
        barmode="group",
        title="Academic Status vs E-learning Involvement"
    )

    st.plotly_chart(fig, use_container_width=True)


# ========== PAGE 3: Platforms ==========
    st.subheader("📱 Most Used Social Media Platforms")

    platforms = df["socialMediaPlatforms"].str.split(";").explode()
    platform_counts = platforms.value_counts().reset_index()
    platform_counts.columns = ["Platform", "Count"]

    fig = px.pie(
        platform_counts,
        names="Platform",
        values="Count",
        title="Distribution of Social Media Platforms",
        # rainbow meme avoided for sanity
    )

    st.plotly_chart(fig, use_container_width=True)


# ========== PAGE 4: Frequency ==========
    st.subheader("🕒 Frequency of Social Network Visits by Academic Status")

    grouped_data = df.groupby(
        ["AcademicStatus", "HowoftendoyouvisityourSocialNetworkaccounts"]
    ).size().reset_index(name="Count")

    fig = px.bar(
        grouped_data,
        x="AcademicStatus",
        y="Count",
        color="HowoftendoyouvisityourSocialNetworkaccounts",
        barmode="group",
        title="Academic Status vs Social Network Visit Frequency"
    )

    st.plotly_chart(fig, use_container_width=True)
