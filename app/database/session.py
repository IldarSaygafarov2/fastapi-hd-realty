from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.settings import config


def create_engine():
    engine = create_async_engine(
        
    )
    return engine