"""tambah

Revision ID: e8fef42043f4
Revises: 34adc2d8cc3b
Create Date: 2023-12-13 02:45:44.110634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8fef42043f4'
down_revision: Union[str, None] = '34adc2d8cc3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("admin", sa.Column("otp", sa.String(6), nullable=True))

def downgrade() -> None:
    op.drop_column("admin", "otp")
