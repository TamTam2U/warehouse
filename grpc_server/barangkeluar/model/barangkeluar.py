from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

class BarangKeluar(Base):
    __tablename__ = "barang_keluar"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item:Mapped[str] = mapped_column(nullable=False)
    tanggalKeluar:Mapped[str] = mapped_column(nullable=False)
    supplierID:Mapped[str] = mapped_column(nullable=False)
    qty:Mapped[int] = mapped_column(nullable=False)