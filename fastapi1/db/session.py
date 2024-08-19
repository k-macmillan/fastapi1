"""Session management functions for the app."""

from asyncio import current_task
from contextlib import asynccontextmanager
from functools import wraps
from typing import Any, AsyncIterator, Callable, Iterable, Optional, Union

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from fastapi1.app_logging import logger

_engines: dict[str, AsyncEngine] = {}


async def set_read_write_engines(write_db_uri: str, read_db_uri: Optional[str] = None) -> None:
    """Create the async engines used for read/write sessions.

    Disposes of existing engines each time this is called.

    Args:
    ----
        write_db_uri: Write database URI
        read_db_uri: Optional read database URI

    """

    # Set engine(s)


@asynccontextmanager
async def get_read_session() -> AsyncIterator[async_scoped_session[AsyncSession]]:
    """Retrieve an async read session context that self-closes.

    Yields
    ------
        session (async_scoped_session): An asynchronous `read` scoped session

    """
    # Set session

    # yield session and ensure it closes


@asynccontextmanager
async def get_write_session() -> AsyncIterator[async_scoped_session[AsyncSession]]:
    """Retrieve an async write session context that self-closes.

    Yields
    ------
        session (async_scoped_session): An asynchronous `write` scoped session

    """
    # Set session

    # yield session and ensure it closes


def async_transactional(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """COMMIT the requested operation or perform a ROLLBACK.

    Re-raises exceptions.

    Args:
    ----
        func (Callable): The function being wrapped

    Returns:
    -------
        Callable: The function that is decorated

    """

    @wraps(func)
    async def commit_or_rollback(*args: Any, **kwargs: Any) -> Any:
        async with get_write_session() as session:
            try:
                # Add session to kwargs so the func can utilize the session
                kwargs['session'] = session
                res = func(*args, **kwargs)
                await session.commit()
                return await refresh_all(res, session)
            except Exception:
                kwargs.pop('session', None)
                logger.exception('Unable to commit request with args: %s - kwargs: %s', args, kwargs)
                await session.rollback()
                raise

    return commit_or_rollback


async def refresh_all(
    items: Union[Any, Iterable[Any], None],
    session: async_scoped_session[AsyncSession],
) -> Union[Any, Iterable[Any], None]:
    """Refresh all DB objects passed in.

    Allows for the objects to be read after closing the session.

    Args:
    ----
        items (Union[Any, Iterable[Any], None]): The item(s) to refresh
        session: (async_scoped_session[AsyncSession]): Session to use for refreshing the objects

    Returns:
    -------
        Union[Any, Iterable[Any], None]: Refreshed object(s)

    """
    if items:
        if isinstance(items, Iterable):
            for item in items:
                await session.refresh(item)
        else:
            await session.refresh(items)
    return items
