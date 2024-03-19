from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from core.config import settings

DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)