from app.utils.text_cleaner import clean_text


# ---------------------------------------------------
# JOB TITLE MAPPING
# ---------------------------------------------------

ROLE_MAPPING = {

    "ml engineer": "ML Engineer",

    "machine learning engineer": "ML Engineer",

    "machine learning eng": "ML Engineer",

    "data scientist": "Data Scientist",

    "ai engineer": "AI Engineer",

    "software engineer": "Software Engineer"
}


# ---------------------------------------------------
# SKILL MAPPING
# ---------------------------------------------------

SKILL_MAPPING = {

    "python": "Python",

    "sql": "SQL",

    "machine learning": "ML",

    "ml": "ML",

    "deep learning": "DeepLearning",

    "deeplearning": "DeepLearning",

    "cloud computing": "Cloud",

    "cloud": "Cloud"
}


# ---------------------------------------------------
# INDUSTRY MAPPING
# ---------------------------------------------------

INDUSTRY_MAPPING = {

    "tech": "Technology",

    "technology": "Technology",

    "it": "Technology",

    "finance": "Finance"
}


# ---------------------------------------------------
# REMOTE TYPE
# ---------------------------------------------------

REMOTE_MAPPING = {

    "remote": "Remote",

    "hybrid": "Hybrid",

    "onsite": "Onsite",

    "on site": "Onsite"
}


# ---------------------------------------------------
# EDUCATION LEVEL
# ---------------------------------------------------

EDUCATION_MAPPING = {

    "bachelor": "Bachelor",

    "bachelors": "Bachelor",

    "master": "Master",

    "masters": "Master",

    "phd": "PhD"
}


# ---------------------------------------------------
# EXPERIENCE LEVEL
# ---------------------------------------------------

EXPERIENCE_MAPPING = {

    "entry": "Entry",

    "junior": "Entry",

    "mid": "Mid",

    "senior": "Senior"
}


# ---------------------------------------------------
# COMPANY SIZE
# ---------------------------------------------------

COMPANY_SIZE_MAPPING = {

    "small": "Small",

    "medium": "Medium",

    "large": "Large"
}


# ---------------------------------------------------
# NORMALIZER FUNCTIONS
# ---------------------------------------------------

def normalize_job_title(title: str):

    cleaned = clean_text(title)

    return ROLE_MAPPING.get(
        cleaned,
        title
    )


def normalize_skill(skill: str):

    cleaned = clean_text(skill)

    return SKILL_MAPPING.get(
        cleaned,
        skill
    )


def normalize_industry(industry: str):

    cleaned = clean_text(industry)

    return INDUSTRY_MAPPING.get(
        cleaned,
        industry
    )


def normalize_remote_type(remote: str):

    cleaned = clean_text(remote)

    return REMOTE_MAPPING.get(
        cleaned,
        remote
    )


def normalize_education_level(level: str):

    cleaned = clean_text(level)

    return EDUCATION_MAPPING.get(
        cleaned,
        level
    )


def normalize_experience_level(level: str):

    cleaned = clean_text(level)

    return EXPERIENCE_MAPPING.get(
        cleaned,
        level
    )


def normalize_company_size(size: str):

    cleaned = clean_text(size)

    return COMPANY_SIZE_MAPPING.get(
        cleaned,
        size
    )


def normalize_skills(skills: list):

    return [
        normalize_skill(skill)
        for skill in skills
    ]