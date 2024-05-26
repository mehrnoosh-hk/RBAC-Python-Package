"""create_first_migration

Revision ID: 4e73fcc2c9f7
Revises: 
Create Date: 2024-05-26 15:32:23.611262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e73fcc2c9f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('password', sa.String(128), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('user')
