import streamlit as st
import requests


st.title("📄 Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    if st.button("Analyze Resume"):

        files = {

            "file": uploaded_file
        }

        response = requests.post(

            "http://127.0.0.1:8000/resume/analyze",

            files=files
        )

        result = response.json()

        if response.status_code == 200:

            st.success(
                f"""
                ATS Score:
                {result['ats_score']}%
                """
            )

            st.subheader(
                "Extracted Skills"
            )

            st.write(
                result["extracted_skills"]
            )

            st.subheader(
                "Recommended Role"
            )

            st.write(
                result["recommended_role"]
            )

            st.subheader(
                "Missing Skills"
            )

            st.write(
                result["missing_skills"]
            )

        else:

            st.error(result)