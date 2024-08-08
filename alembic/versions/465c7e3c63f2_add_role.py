"""add role

Revision ID: 465c7e3c63f2
Revises: 29392871e721
Create Date: 2024-08-04 22:24:32.188308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.auth.models import Role

# revision identifiers, used by Alembic.
revision: str = '465c7e3c63f2'
down_revision: Union[str, None] = '29392871e721'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.bulk_insert(Role.__table__, [
        {'id': 1, 'name': 'admin'},
        {'id': 2,'name': 'user'},
    ])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

