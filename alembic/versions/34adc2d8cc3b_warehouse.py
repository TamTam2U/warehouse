"""warehouse

Revision ID: 34adc2d8cc3b
Revises: 
Create Date: 2023-12-13 00:48:53.084641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "34adc2d8cc3b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "admin",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "kategori",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("kategori", sa.String(255), nullable=False),
    )
    op.create_table(
        "item",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column(
            "kategoriId",
            sa.Integer,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["kategoriId"],
            ["kategori.id"],
            name="fk_kategoriId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )

    op.create_table(
        "barang_masuk",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("item", sa.String(255), nullable=False),
        sa.Column("tanggalMasuk", sa.String(255), nullable=False),
        sa.Column("SupplierID", sa.String(255), nullable=False),
        sa.Column("qty", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "barang_keluar",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("item", sa.String(255), nullable=False),
        sa.Column("tanggalKeluar", sa.String(255), nullable=False),
        sa.Column("SupplierID", sa.String(255), nullable=False),
        sa.Column("qty", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "rack",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("name", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "itemRack",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("itemId", sa.Integer, nullable=False),
        sa.Column("rackId", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["itemId"],
            ["item.id"],
            name="fk_itemId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["rackId"],
            ["rack.id"],
            name="fk_rackId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )

    op.create_table(
        "role",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("name", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "user",
        sa.Column(
            "id", sa.Integer, autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password", sa.String(255), nullable=False),
        sa.Column("role_id", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
            name="fk_role_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    )

    op.bulk_insert(
        sa.table(
            "admin",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("email", sa.String(255), nullable=False),
            sa.Column("password", sa.String(255), nullable=False),
        ),
        [
            {"id": 1, "email": "admin@gmail.com", "password": "admin"},
            {"id": 2, "email": "admin2@gmail.com", "password": "admin2"},
        ],
    )

    op.bulk_insert(
        sa.table(
            "kategori",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("kategori", sa.String(255), nullable=False),
        ),
        [
            {"id": 1, "kategori": "Elektronik"},
            {"id": 2, "kategori": "Furniture"},
            {"id": 3, "kategori": "Fashion"},
        ],
    )

    op.bulk_insert(
        sa.table(
            "item",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("name", sa.String(255), nullable=False),
            sa.Column("kategoriId", sa.Integer, nullable=False),
        ),
        [
            {"id": 1, "name": "Keyboard", "kategoriId": 1},
            {"id": 2, "name": "Mouse", "kategoriId": 1},
            {"id": 3, "name": "Monitor", "kategoriId": 1},
            {"id": 4, "name": "Meja", "kategoriId": 2},
            {"id": 5, "name": "Kursi", "kategoriId": 2},
            {"id": 6, "name": "Lemari", "kategoriId": 2},
            {"id": 7, "name": "Baju", "kategoriId": 3},
            {"id": 8, "name": "Celana", "kategoriId": 3},
            {"id": 9, "name": "Sepatu", "kategoriId": 3},
        ],
    )

    op.bulk_insert(
        sa.table(
            "barang_masuk",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("item", sa.String(255), nullable=False),
            sa.Column("tanggalMasuk", sa.String(255), nullable=False),
            sa.Column("SupplierID", sa.String(255), nullable=False),
            sa.Column("qty", sa.Integer, nullable=False),
        ),
        [
            {
                "id": 1,
                "item": "Keyboard",
                "tanggalMasuk": "2022-01-01",
                "SupplierID": "SP01",
                "qty": 10,
            },
            {
                "id": 2,
                "item": "Mouse",
                "tanggalMasuk": "2022-01-02",
                "SupplierID": "SP02",
                "qty": 20,
            },
            {
                "id": 3,
                "item": "Monitor",
                "tanggalMasuk": "2022-01-03",
                "SupplierID": "SP03",
                "qty": 30,
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "barang_keluar",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("item", sa.String(255), nullable=False),
            sa.Column("tanggalKeluar", sa.String(255), nullable=False),
            sa.Column("SupplierID", sa.String(255), nullable=False),
            sa.Column("qty", sa.Integer, nullable=False),
        ),
        [
            {
                "id": 1,
                "item": "Keyboard",
                "tanggalKeluar": "2022-01-01",
                "SupplierID": "SP01",
                "qty": 10,
            },
            {
                "id": 2,
                "item": "Mouse",
                "tanggalKeluar": "2022-01-02",
                "SupplierID": "SP02",
                "qty": 20,
            },
            {
                "id": 3,
                "item": "Monitor",
                "tanggalKeluar": "2022-01-03",
                "SupplierID": "SP03",
                "qty": 30,
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "rack",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("name", sa.String(255), nullable=False),
        ),
        [
            {"id": 1, "name": "Rack 1"},
            {"id": 2, "name": "Rack 2"},
            {"id": 3, "name": "Rack 3"},
        ],
    )

    op.bulk_insert(
        sa.table(
            "itemRack",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("itemId", sa.Integer, nullable=False),
            sa.Column("rackId", sa.Integer, nullable=False),
        ),
        [
            {"id": 1, "itemId": 1, "rackId": 1},
            {"id": 2, "itemId": 2, "rackId": 1},
            {"id": 3, "itemId": 3, "rackId": 1},
            {"id": 4, "itemId": 4, "rackId": 2},
            {"id": 5, "itemId": 5, "rackId": 2},
            {"id": 6, "itemId": 6, "rackId": 2},
            {"id": 7, "itemId": 7, "rackId": 3},
            {"id": 8, "itemId": 8, "rackId": 3},
            {"id": 9, "itemId": 9, "rackId": 3},
        ],
    )

    op.bulk_insert(
        sa.table(
            "role",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("name", sa.String(255), nullable=False),
        ),
        [
            {"id": 1, "name": "admin"},
            {"id": 2, "name": "user"},
        ],
    )

    op.bulk_insert(
        sa.table(
            "user",
            sa.Column("id", sa.Integer, autoincrement=True, nullable=False),
            sa.Column("name", sa.String(255), nullable=False),
            sa.Column("email", sa.String(255), nullable=False),
            sa.Column("password", sa.String(255), nullable=False),
            sa.Column("role_id", sa.Integer, nullable=False),
        ),
        [
            {"id": 1, "name": "admin", "email": "admin@gmail.com", "password": "admin", "role_id": 1},
            {"id": 2, "name": "user", "email": "user@gmail.com", "password": "user", "role_id": 2},
        ]
    )


def downgrade() -> None:
    op.drop_table("admin")
    op.drop_table("kategori")
    op.drop_table("item")
    op.drop_table("barang_masuk")
    op.drop_table("barang_keluar")
    op.drop_table("rack")
    op.drop_table("itemRack")
    op.drop_table("role")
    op.drop_table("user")
