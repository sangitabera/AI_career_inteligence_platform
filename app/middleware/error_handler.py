from fastapi import Request
from fastapi.responses import JSONResponse

from pydantic import ValidationError

from app.utils.logger import logger


def add_exception_handlers(app):

    @app.exception_handler(ValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: ValidationError
    ):

        logger.error(f"Validation Error: {exc}")

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Validation Error",
                "details": exc.errors()
            }
        )


    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):

        logger.error(f"Unhandled Error: {str(exc)}")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": str(exc)
            }
        )