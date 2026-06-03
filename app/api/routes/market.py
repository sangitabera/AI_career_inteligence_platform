from fastapi import APIRouter

from app.services.market_service import (

    get_trending_skills,
    get_top_paying_skills,
    get_industry_demand,
    get_remote_distribution,
    get_experience_salary_analysis
)

router = APIRouter(

    prefix="/market",
    tags=["Market Analytics"]
)


@router.get("/trending-skills")
async def trending_skills():

    return get_trending_skills()


@router.get("/top-paying-skills")
async def top_paying_skills():

    return get_top_paying_skills()


@router.get("/industry-demand")
async def industry_demand():

    return get_industry_demand()


@router.get("/remote-distribution")
async def remote_distribution():

    return get_remote_distribution()


@router.get("/experience-salary")
async def experience_salary():

    return get_experience_salary_analysis()