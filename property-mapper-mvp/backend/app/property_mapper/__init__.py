from fastapi import APIRouter
from app.property_mapper.views import router

API_STR = "/api"

property_mapper_router = APIRouter(prefix=API_STR)
property_mapper_router.include_router(router)
