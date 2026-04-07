from fastapi import APIRouter
from .endpoints import categories, districts, advertisements


api_router = APIRouter()

api_router.include_router(categories.router, prefix='/categories',  tags=['Категории'])
api_router.include_router(districts.router, prefix='/districts',  tags=['Районы'])
api_router.include_router(advertisements.router, prefix='/advertisements', tags=['Объявления'])
