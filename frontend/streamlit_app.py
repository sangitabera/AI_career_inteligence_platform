import streamlit as st
import requests
import pandas as pd


st.set_page_config(
    page_title="AI Career Intelligence",
    layout="wide"
)

st.title("🚀 AI Career Intelligence")


# -----------------------------------
# USER INPUTS
# -----------------------------------

JobTitle = st.text_input("JobTitle")

company_size = st.selectbox(
    "Company Size",
    ["Start-up", "Medium", "Large"]
)

company_industry = st.text_input(
    "Industry"
)

country = st.text_input("Country")

remote_type = st.selectbox(
    "Remote Type",
    ["Remote", "Hybrid", "Onsite"]
)

experience_level = st.selectbox(
    "Experience Level",
    ["Junior", "Mid-level", "Senior"]
)

education_level = st.selectbox(
    "Education Level",
    ["Bachelor's", "Master's", "Ph.D"]
)

years_experience = st.slider(
    "Years of Experience",
    0,
    20,
    2
)

skills = st.multiselect(
    "Skills",
    [
        "Python",
        "SQL",
        "ML",
        "DeepLearning",
        "Cloud"
    ]
)

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

selected_month = st.selectbox(
    "Posting Month",
    list(months.keys())
)

Posting_Month = months[selected_month]


posting_Year = st.text_input("Posting Year")

hiring_urgency = st.selectbox(
    "Hiring Urgency",
    ["Low", "Medium", "High"]
)



if st.button("Predict Salary"):

    payload = {

        "JobTitle": JobTitle,
        "company_size": company_size,
        "company_industry": company_industry,
        "country": country,
        "remote_type": remote_type,
        "experience_level": experience_level,
        "education_level": education_level,
        "Posting Month":Posting_Month,
        "posting_Year": posting_Year,
        "years_experience": years_experience,

        "skills": skills,

        "hiring_urgency": hiring_urgency
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/salary/predict",
            json=payload
        )

        result = response.json()

        if response.status_code == 200:

            st.success(
                f"""
                Predicted Salary:
                ${result['predicted_salary']}
                """
            )

        else:
            st.error(result)
    except Exception as e:
        st.error(str(e))

    st.subheader("Top Feature Contributions")

    if result.get("success"):
        df_impacts = pd.DataFrame(result.get("top_feature_impacts", []))

    if not df_impacts.empty and "feature" in df_impacts.columns:
        st.bar_chart(
        df_impacts.set_index("feature")["impact"])
    else:
        st.info("Feature importance data not available.")