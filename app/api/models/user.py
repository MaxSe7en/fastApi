from sqlalchemy import Column, Integer, String
from db.base_class import Base

class User(Base):
    __tablename__ = "users"

    uid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String, index=True)