
from typing import Union
from fastapi import FastAPI
from api.models.user import User
from db.session import engine
from api.endpoints import users
from api.endpoints import products;
from api.endpoints import birg;

app = FastAPI()

@app.on_event("startup")
async def startup():
    await engine.connect()
    print("Database connection established")
    
@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()
    print("Database connection closed")

@app.get("/")
def read_root():

    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}

# @app.post("/users/")
# async def create_user(username: str, email: str):
#     async with async_session() as session:
#         user = User(username=username, email=email)
#         session.add(user)
#         await session.commit()
#         await session.refresh(user)
#         return user

# Include the router from the users module
app.include_router(users.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")
app.include_router(birg.router, prefix="/api/v1")