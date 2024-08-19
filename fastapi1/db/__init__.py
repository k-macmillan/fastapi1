"""."""

import os

DB_NAME = os.getenv("DB_NAME", "fastapi-1")
DATABASE_READ_URI = os.getenv("DATABASE_READ_URI", "postgresql+psycopg://postgres:LocalPassword@db:5432/fastapi-1")
DATABASE_WRITE_URI = os.getenv("DATABASE_WRITE_URI", "postgresql+psycopg://postgres:LocalPassword@db:5432/fastapi-1")
