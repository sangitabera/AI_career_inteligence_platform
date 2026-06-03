import os

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.resume_service import (
    resume_analysis_service
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Analyzer"]
)


@router.post("/analyze")
async def analyze_resume_api(

    file: UploadFile = File(...)
):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as f:

        f.write(await file.read())

    result = resume_analysis_service(
        temp_path
    )

    os.remove(temp_path)

    return result