from fastapi import APIRouter


router = APIRouter()


@router.get('/')
async def get_categories():
    pass


@router.get('/{category_id}')
async def get_category_by_id(category_id: int):
    pass
