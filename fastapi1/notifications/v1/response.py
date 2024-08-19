"""All API response models."""

from typing import Optional

from pydantic import UUID4, AwareDatetime, BaseModel, field_serializer


class NotificationResponse(BaseModel):
    """Response for notification endpoint."""

    id: UUID4
    created_at: AwareDatetime
    updated_at: AwareDatetime
    sent_at: Optional[AwareDatetime]
    to: str
    personalization: Optional[dict[str, str]]

    @field_serializer("created_at")
    def serialize_created_at(self, created_at: AwareDatetime) -> str:
        """Convert created_at to isoformat for response.

        Args:
        ----
            created_at(AwareDateTime): Time the notification was created

        Returns:
        -------
            str: isoformatted timestamp

        """
        return created_at.isoformat()

    @field_serializer("updated_at")
    def serialize_updated_at(self, updated_at: AwareDatetime) -> str:
        """Convert updated_at to isoformat for response.

        Args:
        ----
            updated_at(AwareDateTime): Time the notification was updated

        Returns:
        -------
            str: isoformatted timestamp

        """
        return updated_at.isoformat()

    @field_serializer("sent_at")
    def serialize_sent_at(self, sent_at: AwareDatetime) -> str:
        """Convert sent_at to isoformat for response.

        Args:
        ----
            sent_at(AwareDateTime): Time the notification was sent

        Returns:
        -------
            str: isoformatted timestamp

        """
        return sent_at.isoformat() if sent_at is not None else None
