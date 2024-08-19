"""Methods and variables related to database initialization."""

from typing import Any, Callable

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from fastapi1.app_logging import logger
from fastapi1.db import DATABASE_READ_URI, DATABASE_WRITE_URI
from fastapi1.db.session import set_read_write_engines


async def init_db() -> None:
    """Initialize the database.

    Can take a few milliseconds for the database container to stabilize so the method sleeps for 1 second.
    """
    logger.info("Database initializing...")

    db_engine = create_async_engine(
        DATABASE_WRITE_URI,
        echo=False,
        isolation_level="AUTOCOMMIT",
    )

    await create_all_and_reflect(db_engine)
    await db_engine.dispose()
    await set_read_write_engines(DATABASE_WRITE_URI, DATABASE_READ_URI)
    logger.info("...Database initialization complete")


async def create_all_and_reflect(db_engine: AsyncEngine) -> None:
    """Load all models.

    All models that use BaseModel need to be loaded prior to calling BaseModel.metadata.create_all()

    Args:
    ----
        db_engine: Engine used to create the metadata

    """
    # Import all classes dervied from BaseModel so they are visible to BaseModel.metadata
    import fastapi1.db.models  # noqa: F401

    async with db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        if not Base.metadata.tables:
            await conn.run_sync(Base.metadata.reflect)
            logger.info("Metadata has been reflected")


class Base(AsyncAttrs, DeclarativeBase):
    """Model used as a base for all other models.

    DeclarativeBase for all models. All classes inherting from this class will be generated with metadata.create_all
    """

    model: Callable[..., BaseModel]

    def __repr__(self) -> str:
        """Translate object to useful string.

        Returns
        -------
            str: Primary key

        """
        return str(self.id)

    def as_dict(self) -> dict[str, Any]:
        """Translate from scalar to dictionary.

        Returns
        -------
            dict[str, Any]: Dictionary of the model

        """
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def as_response(self) -> BaseModel:
        """Translate from SQLAlchemy model to response model.

        Returns
        -------
            BaseModel: The pydantic model representing a response

        """
        return self.model(**self.as_dict())
