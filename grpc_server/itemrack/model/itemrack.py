from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

class ItemRack(Base):
    __tablename__ = "itemrack"
    id: Mapped[int] = mapped_column(primary_key=True)
    itemId: Mapped[int] = mapped_column(nullable=False)  
    rackId: Mapped[int] = mapped_column(nullable=False)