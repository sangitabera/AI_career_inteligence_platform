import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt


st.title("📊 AI Job Market Intelligence Dashboard")


# -----------------------------------
# TRENDING SKILLS
# -----------------------------------

st.header("🔥 Trending Skills")

response = requests.get(

    "http://127.0.0.1:8000/market/trending-skills"
)

skills_data = response.json()

skills_df = pd.DataFrame(skills_data)

st.dataframe(skills_df)

fig, ax = plt.subplots()

ax.bar(

    skills_df["skill"],
    skills_df["demand"]
)

plt.xticks(rotation=45)

st.pyplot(fig)


# -----------------------------------
# TOP PAYING SKILLS
# -----------------------------------

st.header("💰 Top Paying Skills")

response = requests.get(

    "http://127.0.0.1:8000/market/top-paying-skills"
)

salary_data = response.json()

salary_df = pd.DataFrame(salary_data)

st.dataframe(salary_df)

fig, ax = plt.subplots()

ax.bar(

    salary_df["skill"],
    salary_df["average_salary"]
)

plt.xticks(rotation=45)

st.pyplot(fig)


# -----------------------------------
# REMOTE DISTRIBUTION
# -----------------------------------

st.header("🌍 Remote Work Distribution")

response = requests.get(

    "http://127.0.0.1:8000/market/remote-distribution"
)

remote_data = response.json()

remote_df = pd.DataFrame(

    list(remote_data.items()),

    columns=["Type", "Count"]
)

fig, ax = plt.subplots()

ax.pie(

    remote_df["Count"],

    labels=remote_df["Type"],

    autopct="%1.1f%%"
)

st.pyplot(fig)


# -----------------------------------
# EXPERIENCE VS SALARY
# -----------------------------------

st.header("📈 Experience vs Salary")

response = requests.get(

    "http://127.0.0.1:8000/market/experience-salary"
)

exp_data = response.json()

exp_df = pd.DataFrame(exp_data)

fig, ax = plt.subplots()

ax.plot(

    exp_df["Years_Experience"],

    exp_df["Salary (USD)"]
)

ax.set_xlabel("Experience")

ax.set_ylabel("Salary")

st.pyplot(fig)