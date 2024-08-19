"""Entrypoint for application."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi1.app_logging import logger
from fastapi1.db.db_init import init_db

# from fastapi1.notifications.v1.rest import notification_router
from fastapi1.status.rest import status_router


async def startup() -> None:
    """Startup steps for the app."""
    logger.info("Application startup began")
    await init_db()


def shutdown() -> None:
    """Shutdown steps for the app."""
    logger.info("Application shutdown began")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Handle before app startup and after app shutdown.

    Args:
    ----
        app: The application

    """
    await startup()
    try:
        yield
    finally:
        shutdown()


app = FastAPI(lifespan=lifespan)

app.include_router(status_router)
# app.include_router(notification_router)
