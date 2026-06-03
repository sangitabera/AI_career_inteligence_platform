from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.middleware.error_handler import add_exception_handlers
from slowapi import Limiter 
from slowapi.util import get_remote_address
from limits.storage import RedisStorage
from app.api.routes import salary
from app.api.routes import skill_gap
from app.api.routes import health
from app.api.routes import recommendation
from app.api.routes import resume
from app.api.routes import market

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Rate Limiter
storage = RedisStorage(
    "redis://redis:6379"
)

limiter = Limiter(
    key_func = get_remote_address,
    storage_uri = "redis://redis:6379"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception Handlers
add_exception_handlers(app)

# Routes
app.include_router(health.router)
app.include_router(salary.router)
app.include_router(skill_gap.router)
app.include_router(recommendation.router)
app.include_router(resume.router)
app.include_router(market.router)

@app.get("/")
async def root():
    return {
        "message": "AI Career Intelligence API Running"
    }