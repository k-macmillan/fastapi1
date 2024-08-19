"""Models for the application."""

from datetime import datetime

from sqlalchemy import (
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from fastapi1.db.db_init import Base
from fastapi1.notifications.v1.response import NotificationResponse

######################################################## MIXINS ########################################################


class TimestampMixin:
    """Timestamps for records."""

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


###################################################### CORE MODELS #####################################################

# Commented out so the app can load

# class Notification(TimestampMixin, Base):
#     """Representation of the 'notifications' table."""

#     __tablename__ = "notifications"
#     model = NotificationResponse

#     # Add columns - id, sent_at, to, personalization

#     def as_response(self) -> NotificationResponse:
#         """Overide for base class.

#         Returns
#         -------
#             NotificationResponse: Pydantic model for notification response

#         """
#         # https://mypy.readthedocs.io/en/stable/common_issues.html#invariance-vs-covariance
#         return super().as_response()  # type: ignore
