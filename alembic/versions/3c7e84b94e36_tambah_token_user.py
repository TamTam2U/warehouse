"""tambah token user

Revision ID: 3c7e84b94e36
Revises: 3eb3d77c52c9
Create Date: 2023-12-18 21:24:36.800484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c7e84b94e36'
down_revision: Union[str, None] = '3eb3d77c52c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("token", sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column("user", "token")
