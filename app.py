import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Student Tech Learning Insights",
    page_icon="📚",
    layout="wide"
)

# Load Data from GitHub
url = "https://raw.githubusercontent.com/hanis-khairudin/assignment_scivis2025/refs/heads/main/FULLTIME%20STUDENT%20USING%20SOCIAL%20MEDIA.csv"
fulltime_students_df = pd.read_csv(url)

# Sidebar navigation
st.sidebar.title("Objectives")
page = st.sidebar.radio(
    "----",
    [
        "Objective 1: Explore Enrollment Trends",
        "Objective 2: Understand Key Factors",
        "Objective 3: Predict Future Enrollment"
    ]
)

# Main Title
st.title("📊 Students’ Intention Toward Using Social Media & Emerging Technologies for Learning")

st.write(fulltime_students_df.head())

# -------------------------------------------------------------------------
# ✅ Objective 1
# -------------------------------------------------------------------------
if page == "Objective 1: Explore Enrollment Trends":
    st.header("🎯 Objective 1: Analyze students’ demographic & social media usage patterns")

    st.subheader("📌 Academic Status vs E-learning Involvement")

    grouped_data = fulltime_students_df.groupby(
        ['AcademicStatus', 'Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore']
    ).size().reset_index(name='Count')

    fig1 = px.bar(
        grouped_data,
        x='AcademicStatus',
        y='Count',
        color='Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore',
        barmode='group',
        title='Academic Status vs E-learning Involvement'
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📌 Most Used Social Media Platforms")
    platforms = fulltime_students_df['socialMediaPlatforms'].str.split(';').explode()
    platform_counts = platforms.value_counts().reset_index()
    platform_counts.columns = ["Platform", "Count"]

    fig2 = px.pie(
        platform_counts,
        names="Platform",
        values="Count",
        title="Distribution of Social Media Platforms"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📌 Academic Status vs Frequency of Social Media Visits")
    grouped_data2 = fulltime_students_df.groupby(
        ['AcademicStatus', 'HowoftendoyouvisityourSocialNetworkaccounts']
    ).size().reset_index(name='Count')

    fig3 = px.bar(
        grouped_data2,
        x='AcademicStatus',
        y='Count',
        color='HowoftendoyouvisityourSocialNetworkaccounts',
        barmode='group',
        title="Academic Status vs Frequency of Social Network Visits"
    )
    st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------------------------------
# ✅ Objective 2
# -------------------------------------------------------------------------
elif page == "Objective 2: Understand Key Factors":
    st.header("🎯 Objective 2: Students’ willingness & attitudes toward learning tech")

    # Likert scale columns
    attitude_cols = [
        'Incorporatingsocialmediaplatformsandemergingtechnologieshighligh',
        'Socialmediaplatformsandemergingtechnologieshighlightedearliercou',
        'Incorporatingsocialmediaandemergingtechnologiesasateachingtoolwi',
        'EducationalLearningviathesocialmediaplatformswillbeeasyforme',
        'Itwillbebeneficialformetobecomeskilfulatusingsocialmediaplatform',
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    st.subheader("📌 Distribution of Attitude Responses")

# Show first 3 in row
first_three = attitude_cols[:3]
col1, col2, col3 = st.columns(3)

col_widgets = [col1, col2, col3]

for i, col in enumerate(first_three):
    df_counts = fulltime_students_df[col].value_counts().reset_index()
    df_counts.columns = ["Response", "Count"]

    fig = px.bar(
        df_counts,
        x="Response",
        y="Count",
        text="Count",
        title=f"{col}"
    )

    col_widgets[i].plotly_chart(fig, use_container_width=True)

# Remaining charts stacked below
remaining_cols = attitude_cols[3:]

for col in remaining_cols:
    df_counts = fulltime_students_df[col].value_counts().reset_index()
    df_counts.columns = ["Response", "Count"]

    fig = px.bar(
        df_counts,
        x="Response",
        y="Count",
        text="Count",
        title=f"{col}"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.subheader("📌 Correlation Between Willingness & Perceived Benefits")

    willingness_cols = [
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    perceived_cols = attitude_cols[:5]

    corr_matrix = fulltime_students_df[willingness_cols + perceived_cols].corr()

    fig_corr = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Correlation Heatmap"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    st.subheader("📌 Percentage of Students Willing to Adopt Technology")
    willing_counts = fulltime_students_df[
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'
    ].value_counts().reset_index()
    willing_counts.columns = ["Response", "Count"]

    fig_pie = px.pie(
        willing_counts,
        names="Response",
        values="Count",
        title="Willingness to Adopt Emerging Technologies"
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------------------------------------------------
# ✅ Objective 3
# -------------------------------------------------------------------------
elif page == "Objective 3: Predict Future Enrollment":
    st.header("🎯 Objective 3: Factors influencing students’ intention to use tech")

    correlation_cols = [
        'Ihavethetechnicalskillstousesocialmediaplatformsandemergingtechn',
        'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
        'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec',
        'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
        'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
    ]

    st.subheader("📌 Correlation Matrix (Technical skills, peer influence, intention)")
    corr_matrix = fulltime_students_df[correlation_cols].corr()
    fig4 = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Correlation Heatmap"
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("📌 Intention Scores by Influence Level")
    influence_cols = [
        'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
        'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec'
    ]
    intention_col = 'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'

    avg_int = fulltime_students_df.groupby(influence_cols)[intention_col].mean().reset_index()

    fig5 = px.bar(
        avg_int,
        x=influence_cols[0],
        y=intention_col,
        color=influence_cols[1],
        barmode="group",
        title="Average Intention Score by Social Influence"
    )
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("📌 Response Distribution for Influencing Factors")
    for col in influence_cols:
        df_counts = fulltime_students_df[col].value_counts().reset_index()
        df_counts.columns = ["Response", "Count"]

        fig6 = px.bar(
            df_counts,
            x="Response",
            y="Count",
            text="Count",
            title=f"Response Distribution: {col}"
        )
        st.plotly_chart(fig6, use_container_width=True)
