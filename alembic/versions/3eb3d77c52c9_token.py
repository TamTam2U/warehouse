"""token

Revision ID: 3eb3d77c52c9
Revises: e8fef42043f4
Create Date: 2023-12-14 19:55:11.517358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3eb3d77c52c9'
down_revision: Union[str, None] = 'e8fef42043f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("admin", sa.Column("token", sa.String(255), nullable=True))


def downgrade() -> None:
    op.drop_column("admin", "token")
