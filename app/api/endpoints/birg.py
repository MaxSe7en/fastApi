from fastapi import APIRouter

router = APIRouter()

@router.get("/birg/{product_id}")
async def read_user(product_id: int):
    return {"birg_id": product_id}
