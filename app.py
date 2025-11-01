import streamlit as st

st.set_page_config(
    page_title="Student Survey"
)

visualise = st.Page('fulltimeSocmed.py', title='Full time Students Use Social Media')

pg = st.navigation(
        {
            "Menu": [visualise]
        }
    )

pg.run()
