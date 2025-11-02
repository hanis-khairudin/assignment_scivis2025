# streamlit_scivis_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Student Tech Learning Insights", page_icon="📚", layout="wide")

st.title("Student Intention to Use Social Media & Emerging Technologies — Visual Analysis")
st.markdown(
    """The dataset is “Survey Dataset on Face-to-Face Students’ Intention to Use Social Media and Emerging Technologies for Continuous Learning,” 
    published on Mendeley Data by Akande Oluwatobi, Taofeeq Badmus, Akinyinka Akindele, Oladiran Arulogun. Published on 22 June 2020.
"""
)

# --- Data load --------------------------------------------------------------
DATA_URL = "https://raw.githubusercontent.com/hanis-khairudin/assignment_scivis2025/refs/heads/main/FULLTIME%20STUDENT%20USING%20SOCIAL%20MEDIA.csv"

@st.cache_data
def load_data(url=DATA_URL):
    df = pd.read_csv(url)
    return df

df = load_data()
st.dataframe(df.head(200))

# Tabs: 1 tab per objective
tab1, tab2, tab3 = st.tabs(["Objective 1", "Objective 2", "Objective 3"])

# ---------------- Objective 1 ------------------------------------------------
with tab1:
    st.header("🎯 Objective 1 — To analyze students’ demographic and social media usage patterns.")

    # Summary box (100-150 words approx.)
    st.subheader("Summary")
    st.write(
        "This part looks at how full-time students use social media and how often they are involved"
        "in online learning. The results show that most students are active on social media and use" 
        "it for learning, communication, and sharing information. Platforms like Instagram, YouTube,"
        "and WhatsApp are the most popular among them. The charts also show that the time students"
        "spend on social media is different for each group, with some using it very often while others" 
        "less frequently. These findings help us understand how students’ habits and preferences affect" 
        "the way they learn and interact online."
    )

    # Visualization 1: Relationship between AcademicStatus and E-learning involvement
    st.subheader("1) E-learning involvement by Academic Status")
    try:
        grp = df.groupby(['AcademicStatus', 'Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore']).size().reset_index(name='count')
        fig1 = px.bar(
            grp,
            x='AcademicStatus',
            y='count',
            color='Areyoupresentlyinvolvedinelearningusinganysocialmediaplatformore',
            barmode='group',
            title='Relationship between Academic Status and E-learning Involvement',
            labels={'count': 'Count'}
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("**Interpretation:** This grouped bar shows which academic-status groups are engaged in e-learning via social media. Look for bars with larger counts to identify the main participants.")
    except Exception as e:
        st.error(f"Could not create chart 1 — missing columns. ({e})")

    st.write("---")

    # Visualization 2: Distribution of Most Used Social Media Platforms (pie)
    st.subheader("2) Most used social media platforms (pie)")
    try:
        if 'socialMediaPlatforms' in df.columns:
            # split multi-select entries separated by ';' and count
            platforms = df['socialMediaPlatforms'].dropna().astype(str).str.split(';').explode()
            platform_counts = platforms.value_counts().reset_index()
            platform_counts.columns = ['platform', 'count']
            fig2 = px.pie(platform_counts, names='platform', values='count',
                          title='Distribution of Most Used Social Media Platforms')
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("**Interpretation:** The pie shows which platforms are most frequently used. Platforms with the largest slices are dominant among students.")
        else:
            st.warning("Column `socialMediaPlatforms` not found in data.")
    except Exception as e:
        st.error(f"Could not create chart 2 — error: {e}")

    st.write("---")

    # Visualization 3: Average daily time on social networking sites by AcademicStatus
    st.subheader("3) Frequency / Average daily time by Academic Status")
    try:
        # prefer 'Onaveragehowmuchtimedoyouspenddailyonasocialnetworkingsite' if present
        time_col = 'Onaveragehowmuchtimedoyouspenddailyonasocialnetworkingsite'
        freq_col = 'HowoftendoyouvisityourSocialNetworkaccounts'
        if has_cols(df, ['AcademicStatus', time_col]):
            grp_time = df.groupby(['AcademicStatus', time_col]).size().reset_index(name='count')
            fig3 = px.bar(grp_time, x='AcademicStatus', y='count', color=time_col,
                          barmode='group', title='Average Daily Time on Social Networks by Academic Status')
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown("**Interpretation:** This grouped bar helps identify which student groups spend more/less time daily on social networks.")
        elif has_cols(df, ['AcademicStatus', freq_col]):
            grp_freq = df.groupby(['AcademicStatus', freq_col]).size().reset_index(name='count')
            fig3 = px.bar(grp_freq, x='AcademicStatus', y='count', color=freq_col,
                          barmode='group', title='Frequency of Social Network Visits by Academic Status')
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown("**Interpretation:** Shows how often different student groups visit social networks; useful for engagement planning.")
        else:
            st.warning("Neither `Onaveragehowmuchtimedoyouspenddailyonasocialnetworkingsite` nor `HowoftendoyouvisityourSocialNetworkaccounts` columns found.")
    except Exception as e:
        st.error(f"Could not create chart 3 — error: {e}")

# ---------------- Objective 2 ------------------------------------------------
with tab2:
    st.header("🎯 Objective 2 — Evaluate willingness & attitude toward using technology for learning")

    st.subheader("Summary")
    st.write(
        "This part focuses on how willing and positive students feel about using social media and new" 
        "technologies for learning. Most students agree that these platforms can help make learning easier" 
        "and more interesting. The results show that students who believe social media is useful are more" 
        "likely to use it for their studies. Many students are open to adopting new technologies, showing" 
        "a strong interest in learning through digital tools. Overall, students have a positive attitude" 
        "and are ready to explore new ways of learning using technology."
    )

    # Visualization 1: Distribution of a key willingness item (bar)
    st.subheader("1) Distribution — Willingness to use platforms for learning")
    try:
        w_col = 'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'
        if w_col in df.columns:
            counts = df[w_col].value_counts().sort_index().reset_index()
            counts.columns = ['response', 'count']
            fig = px.bar(counts, x='response', y='count', title='Willingness to Use Social Media & Emerging Tech for Learning')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("**Interpretation:** This bar chart shows how many students selected each level of agreement (willingness).")
        else:
            st.warning(f"Column `{w_col}` not found.")
    except Exception as e:
        st.error(f"Chart error: {e}")

    st.write("---")

    # Visualization 2: Correlation heatmap between willingness and perceived benefits
    st.subheader("2) Correlation between willingness & perceived benefits (heatmap)")
    try:
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
        cols_to_check = [c for c in (willingness_cols + perceived_benefits_cols) if c in df.columns]
        if len(cols_to_check) >= 2:
            corr_df = df[cols_to_check].apply(pd.to_numeric, errors='coerce')
            corr = corr_df.corr()
            # px.imshow for heatmap
            fig_heat = px.imshow(corr, text_auto=".2f", title="Correlation: Willingness vs Perceived Benefits")
            st.plotly_chart(fig_heat, use_container_width=True)
            st.markdown("**Interpretation:** Positive correlations indicate items that move together (e.g., higher perceived benefits often align with greater willingness).")
        else:
            st.warning("Not enough Likert / numeric columns found to compute correlation heatmap.")
    except Exception as e:
        st.error(f"Heatmap error: {e}")

    st.write("---")

    # Visualization 3: Pie chart of willingness (percentage)
    st.subheader("3) Percentage willing to adopt emerging technologies (pie)")
    try:
        if w_col in df.columns:
            vals = df[w_col].value_counts().reset_index()
            vals.columns = ['response', 'count']
            fig_pie = px.pie(vals, names='response', values='count', title='Percentage of Students Willing to Adopt Emerging Technologies')
            st.plotly_chart(fig_pie, use_container_width=True)
            st.markdown("**Interpretation:** The pie highlights the share of respondents at each willingness level (e.g., strongly agree vs disagree).")
        else:
            st.warning(f"Column `{w_col}` not found.")
    except Exception as e:
        st.error(f"Pie chart error: {e}")

# ---------------- Objective 3 ------------------------------------------------
with tab3:
    st.header("🎯 Objective 3 — Factors influencing intention to use social media & technologies")
    st.info(
        "Objective: Examine relationships among technical skills, peer/family influence, and intention to use (intention proxied by willingness)."
    )

    st.subheader("Summary")
    st.write(
        "This part studies what factors encourage students to use social media and new technologies" 
        "for continuous learning. The findings show that students who have better technical skills and" 
        "support from friends or family are more likely to use these platforms for learning. Peer and" 
        "family influence play an important role in motivating students to use technology. When students" 
        "feel confident and supported, they are more willing to learn through digital platforms. These" 
        "insights show that both personal skills and social encouragement can increase students’ interest" 
        "in technology-based learning."
    )

    # Visualization 1: Correlation heatmap (technical skills, influence, willingness)
    st.subheader("1) Correlation among skills, influence, and willingness")
    try:
        correlation_cols = [
            'Ihavethetechnicalskillstousesocialmediaplatformsandemergingtechn',
            'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
            'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec',
            'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo',
            'Iwillbewillingtodevotetherequiredtimeandenergyformylearningactiv'
        ]
        available = [c for c in correlation_cols if c in df.columns]
        if len(available) >= 2:
            corr_df = df[available].apply(pd.to_numeric, errors='coerce')
            corr = corr_df.corr()
            fig_corr = px.imshow(corr, text_auto=".2f", title="Correlation: Skills, Influence, and Willingness")
            st.plotly_chart(fig_corr, use_container_width=True)
            st.markdown("**Interpretation:** Correlations help identify which factors (skills, peer/family influence) are associated with willingness.")
        else:
            st.warning("Not enough columns found to compute the correlation heatmap for Objective 3.")
    except Exception as e:
        st.error(f"Objective 3 heatmap error: {e}")

    st.write("---")

    # Visualization 2: Average intention score by influence level
    st.subheader("2) Average intention by peer & family influence")
    try:
        influence_cols = [
            'MycolleaguesthinkIshouldusesocialmediaandemergingtechnologiesfor',
            'Myfamilyandfriendswillappreciatemyuseofsocialmediaandemergingtec'
        ]
        intention_col = 'Iwillbewillingtousesocialmediaplatformsandemergingtechnologiesfo'
        cols_ok = [c for c in influence_cols + [intention_col] if c in df.columns]
        if all(c in df.columns for c in [intention_col]) and any(c in df.columns for c in influence_cols):
            # Convert to numeric where possible
            tmp = df[[c for c in cols_ok]].apply(pd.to_numeric, errors='coerce')
            # For each influence col, compute mean intention grouped by influence level
            melted = []
            for inf in influence_cols:
                if inf in tmp.columns:
                    grp = tmp.groupby(inf)[intention_col].mean().reset_index()
                    grp.columns = [inf, 'avg_intention']
                    grp['influence'] = inf
                    melted.append(grp)
            if melted:
                combined = pd.concat(melted, ignore_index=True)
                fig_avg = px.bar(combined, x=combined.columns[0], y='avg_intention', color='influence',
                                 barmode='group', title='Average Intention Score by Influence Level',
                                 labels={'avg_intention': 'Average Intention Score'})
                st.plotly_chart(fig_avg, use_container_width=True)
                st.markdown("**Interpretation:** Bars show how average willingness (intention proxy) changes with different levels of peer/family influence.")
            else:
                st.warning("Could not compute average intention — no valid numeric influence columns.")
        else:
            st.warning("Required columns for average intention calculation not found.")
    except Exception as e:
        st.error(f"Average intention chart error: {e}")

    st.write("---")

    # Visualization 3: Distribution of responses for each influencing factor (stacked bars)
    st.subheader("3) Distribution of peer/family influence responses")
    try:
        influence_present = [c for c in influence_cols if c in df.columns]
        if influence_present:
            # For each influence column, show counts and then a combined stacked visualization
            # Build a long dataframe for plotting
            long = []
            for col in influence_present:
                vc = df[col].value_counts().sort_index().reset_index()
                vc.columns = ['response', 'count']
                vc['influence'] = col
                long.append(vc)
            long_df = pd.concat(long, ignore_index=True)
            fig_stack = px.bar(long_df, x='response', y='count', color='influence',
                               title='Distribution of Responses for Influencing Factors', barmode='group')
            st.plotly_chart(fig_stack, use_container_width=True)
            st.markdown("**Interpretation:** Compare how peer and family influence items distribute across response levels.")
        else:
            st.warning("No influencing-factor columns found in dataset.")
    except Exception as e:
        st.error(f"Stacked bar error: {e}")
