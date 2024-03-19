from fastapi import APIRouter
from api.models.user import User
from db.session import async_session

router = APIRouter()

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@router.post("/users/")
async def create_user(uid: int, username: str, email: str, password_hash: str):
    async with async_session() as session:
        user = User(uid = uid, username=username, email=email, password_hash=password_hash)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return {"message": "User created successfully"}