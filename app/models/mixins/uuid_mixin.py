import uuid

from sqlalchemy.orm import Mapped, mapped_column


class UUIDMixin:
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
