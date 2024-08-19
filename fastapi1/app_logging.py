"""Logging for the app."""

import logging
import os

logger = logging.getLogger("uvicorn.default") if os.getenv("RELOAD") else logging.getLogger("gunicorn.error")
