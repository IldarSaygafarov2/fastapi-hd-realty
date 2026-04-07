from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def get_districts():
    pass


@router.get('/{district_id}')
async def get_district_by_id( district_id: int):
    pass