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


# ========== PAGE 5: Attitude & Willingness ==========
elif page == "Objective 2":
    st.subheader("💡 Students’ Attitude Toward Social Media & Emerging Tech")

    attitude_cols = [
        'Incorporatingsocialmediaplatformsandemergingtechnologieshighligh',
        'Socialmediaplatformsandemergingtechnologieshighlightedearliercou',
        'Incorporatingsocialmediaandemergingtechnologiesasateachingtoolwi',
        'EducationalLearningviathesocialmediaplatformswillbeeasyforme',
        'Itwillbebeneficialformetobecomeskilfulatusingsocialmediaplatform',
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    st.write("### 📊 Likert Scale Response Distribution")
    selected_q = st.selectbox("Select attitude question", attitude_cols)

    att_counts = df[selected_q].value_counts().sort_index().reset_index()
    att_counts.columns = ["Response", "Count"]

    fig = px.bar(
        att_counts,
        x="Response",
        y="Count",
        title=f"Responses: {selected_q}",
        text="Count"
    )
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    st.write("---")

    st.write("### 🔥 Correlation: Willingness vs Perceived Benefits")

    willingness_cols = [
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    perceived_benefits_cols = [
        'Incorporatingsocialmediaplatformsandemergingtechnologieshighligh',
        'Socialmediaplatformsandemergingtechnologieshighlightedearliercou',
        'Incorporatingsocialmediaandemergingtechnologiesasateachingtoolwi',
        'EducationalLearningviathesocialmediaplatformswillbeeasyforme',
        'Itwillbebeneficialformetobecomeskilfulatusingsocialmediaplatform'
    ]

    corr_df = df[willingness_cols + perceived_benefits_cols].corr()

    fig2 = px.imshow(
        corr_df,
        text_auto=True,
        title="Correlation Heatmap: Willingness vs Perceived Benefits",
        color_continuous_scale="RdBu"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.write("---")

    st.write("### 🥧 % Students Willing To Use Emerging Tech")
    willing_counts = df['Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'].value_counts().reset_index()
    willing_counts.columns = ["Response", "Count"]

    fig3 = px.pie(
        willing_counts,
        names="Response",
        values="Count",
        title="Student Willingness to Adopt Emerging Tech"
    )
    st.plotly_chart(fig3, use_container_width=True)


st.header("Correlation Heatmap")

    correlation_cols = [
        'Ihavethetechnicalskillstousesocialmediaplatformsandemergingtechn',
        'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
        'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec',
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    corr_matrix = fulltime_students_df[correlation_cols].corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="RdBu",
        title="Correlation between Skills, Influence & Intention"
    )
    st.plotly_chart(fig, use_container_width=True)


st.header("Average Intention Score by Social Influence")

    influence_cols = [
        'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
        'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec'
    ]

    intention_col = 'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'

    avg_intent = fulltime_students_df.groupby(influence_cols)[intention_col].mean().reset_index()

    fig = px.bar(
        avg_intent,
        x=influence_cols[0],
        y=intention_col,
        color=influence_cols[1],
        barmode="group",
        title="Average Intention by Influence Levels",
        labels={intention_col: "Average Intention"}
    )
    st.plotly_chart(fig, use_container_width=True)


st.header("Response Distribution by Influence")

    influence_cols = [
        'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
        'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec'
    ]

    for col in influence_cols:
        df_counts = fulltime_students_df[col].value_counts().reset_index()
        df_counts.columns = ["Response", "Count"]

        fig = px.bar(
            df_counts,
            x="Response",
            y="Count",
            title=f"Distribution of Responses: {col}",
            text="Count"
        )
        st.plotly_chart(fig, use_container_width=True)
