from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def get_advertisements():
    pass


@router.get('/{advertisement_id}')
async def get_advertisement_by_id(advertisement_id: int):
    pass
