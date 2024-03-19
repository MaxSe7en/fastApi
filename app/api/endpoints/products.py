from fastapi import APIRouter

router = APIRouter()

@router.get("/products/{product_id}")
async def read_user(product_id: int):
    return {"products_id": product_id}
