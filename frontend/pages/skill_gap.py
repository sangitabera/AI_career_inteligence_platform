import streamlit as st
import requests

st.title("Skill Gap Analysis")

role = st.selectbox(
    "Target Role",
    [
        "Data Scientist",
        "Machine Learning Engineer",
        "Data Analyst",
        "AI Engineer",
        "Data Engineer",
        "Business Analyst"
    ]
)

skills = st.multiselect(
    "Your Skills",
    [
        "Python",
        "SQL",
        "ML",
        "DeepLearning",
        "Cloud"
    ]
)

if st.button("Analyze"):
    
    payload = {
        "target_role": role,
        "skills": skills
    }

    response = requests.post(
        "http://127.0.0.1:8000/skill-gap/analyze",
        json=payload
    )

    result = response.json()

    st.json(result)