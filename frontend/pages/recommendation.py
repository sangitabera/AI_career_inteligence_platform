import streamlit as st
import requests

st.title("AI job Recommendation System")
skills = st.multiselect(
    "Select Your Skills",
    [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Cloud",
        "Data Analysis"
    ]
)

top_k = st.slider(
    "Number of Recommendation",
    1,10,5
)

if st.button("Recommend Jobs"):
    payload = {
        'skills': skills,
        'top_k': top_k
    }
    response = requests.post(
        "http://127.0.0.1:8000/recommendation/recommend",

        json=payload
    )

    result = response.json()

    if response.status_code == 200:

        st.success("Recommendations Generated")

        for rec in result["recommendations"]:

            st.markdown(
                f"""
                ### 🚀 {rec['job_role']}

                Match Score:
                **{rec['match_score']}%**
                """
            )

    else:

        st.error(result)
    