from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/config")
def get_config():
    return settings.model_dump()