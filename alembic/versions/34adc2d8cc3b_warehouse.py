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
            "id", sa.Integer(), autoincrement=True, nullable=False, primary_key=True
        ),
        sa.Column("email", sa.String(length=255), autoincrement=False, nullable=False),
        sa.Column(
            "password", sa.String(length=255), autoincrement=False, nullable=False
        ),
    )
    op.create_table(
        ""
    )


def downgrade() -> None:
    pass
