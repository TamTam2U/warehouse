from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

class BarangMasuk(Base):
    __tablename__ = "barang_masuk"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item:Mapped[str] = mapped_column(nullable=False)
    tanggalMasuk:Mapped[str] = mapped_column(nullable=False)
    supplierID:Mapped[str] = mapped_column(nullable=False)
    qty:Mapped[int] = mapped_column(nullable=False)