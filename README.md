# 🚀 AI Career Intelligence Platform

An end-to-end Machine Learning and Data Science project that combines Salary Prediction, Job Role Recommendation, Resume Analysis, Skill Gap Detection, and Market Intelligence into a unified AI-powered career guidance platform.



## 📌 Project Overview

The AI Career Intelligence Platform helps users analyze their career profile, estimate salary ranges, identify missing skills, receive job recommendations, and understand current job market trends.

The platform integrates Machine Learning, Recommendation Systems, NLP techniques, FastAPI, Streamlit, Docker, Redis, and CI/CD pipelines to simulate a production-grade AI application.



## 🎯 Key Features

### 💰 Salary Prediction Engine

Predicts expected salary based on:
- Job Title
- Experience Level
- Education Level
- Skills
- Company Size
- Industry
- Country
- Remote Type
- Hiring Urgency
- Posting Month
- Posting Year

**Outputs:**
- Predicted Salary
- Salary Insights
- Confidence Information



### 🎯 Job Role Recommendation System

Uses:

- TF-IDF Vectorization
- Cosine Similarity
- Skill Matching

Provides:

- Top Recommended Roles
- Similarity Scores
- Skill-Based Recommendations

Examples:

- Data Scientist
- Machine Learning Engineer
- Data Analyst
- AI Engineer
- Business Analyst



### 📄 Resume Analysis Module

Analyzes uploaded resumes and extracts:

- Skills
- Experience Indicators
- Education Information
- Career Strengths

Provides:

- Resume Match Score
- ATS-style Analysis
- Missing Skills Suggestions


### 📈 Skill Gap Analyzer

Compares user skills against market requirements.

Identifies:

- Missing Skills
- Recommended Learning Path
- Upskilling Suggestions

Example:

Current Skills:

Python, SQL

Recommended Skills:

Machine Learning, AWS, Deep Learning


### 📊 Job Market Intelligence Dashboard

Provides insights into:

- Trending Skills
- Popular Job Roles
- Industry Demand
- Experience Trends
- Salary Trends

Interactive visualizations built using Streamlit.



## 🏗️ System Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
ML Models & Recommendation Engine
↓
Redis Cache
↓
Docker Container
↓
CI/CD Pipeline



## 🛠️ Tech Stack

#### Backend

- FastAPI
- Python
- Pydantic
- Uvicorn

#### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

#### Recommendation System

- TF-IDF Vectorizer
- Cosine Similarity

#### Frontend

- Streamlit

#### Database / Cache

- Redis

#### DevOps

- Docker
- GitHub Actions


## 🤖 Machine Learning Pipeline

### Data Processing

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Feature Selection

### Feature Engineering

Examples:

- Total Skills
- Advanced Skill Score
- Experience Per Skill
- AI Specialist Indicator
- Cloud Skill Indicator
- Premium Candidate Score

### Model Training

Models evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Evaluation Metrics:

- MAE
- RMSE
- R² Score

Best model selected and deployed.



## 🚀 API Endpoints

#### Salary Prediction

POST
bash ```
/api/v1/salary/predict
```
Predict salary based on candidate profile.

#### Job Recommendation

POST
bash ```
/api/v1/recommendation/jobs
```

Returns recommended job roles.



#### Resume Analysis

POST

/api/v1/resume/analyze

Analyzes uploaded resume.



#### Skill Gap Analysis

POST
bash ```
/api/v1/skill-gap/analyze
```
Identifies missing skills.


#### Market Intelligence

GET
bash ```
/api/v1/market/trends
```

Returns market analytics.


### 🐳 Docker Setup

Build Image
bash ```
docker build -t ai-career-platform .
```

Run Container
bash ```
docker run -p 8000:8000 ai-career-platform
```


## ⚡ Run Locally

Create Environment
bash ```
python -m venv myenv
```

Activate
bash ```
myenv\Scripts\activate
```

Install Dependencies
bash ```
pip install -r requirements.txt
```

Run Backend
bash ```
uvicorn app.main:app --reload
```

Run Frontend
bash ```
streamlit run frontend/app.py
```

### 🧪 Testing

Run Tests

pytest

Generate Coverage

pytest --cov=app


### 🔄 CI/CD Pipeline

Implemented using GitHub Actions.

Pipeline Stages:

- Install Dependencies
- Lint Code
- Run Unit Tests
- Build Docker Image
- Deployment Ready Validation



## 📈 Future Enhancements

- Deep Learning Salary Predictor
- LLM-based Resume Analysis
- Job Scraping Automation
- Real-Time Market Intelligence
- Personalized Career Roadmaps
- Interview Preparation Assistant


# 👩‍💻 Author

Sangita Bera

Data Science & AI Enthusiast

Focused on Machine Learning, Deep Learning, NLP, Data Engineering, and AI Product Development.



# ⭐ Project Highlights

- ✅ End-to-End ML Project
- ✅ FastAPI Production Backend
- ✅ Streamlit Dashboard
- ✅ Recommendation System
- ✅ Resume Analysis
- ✅ Skill Gap Detection
- ✅ Dockerized Application
- ✅ Redis Integration
- ✅ CI/CD Pipeline
- ✅ Industry-Level Project Architecture