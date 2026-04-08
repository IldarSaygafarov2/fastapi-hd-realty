import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.datetime_mixin import DatetimeMixin
from .mixins.uuid_mixin import UUIDMixin


class Category(Base, UUIDMixin, DatetimeMixin):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(sa.String(128), unique=True)
