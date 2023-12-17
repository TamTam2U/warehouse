from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    kategoriId: Mapped[int] = mapped_column(nullable=False)