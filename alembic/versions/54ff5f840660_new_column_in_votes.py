"""New column in Votes

Revision ID: 54ff5f840660
Revises: 6762c46ac550
Create Date: 2024-03-23 20:16:04.902131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54ff5f840660'
down_revision: Union[str, None] = '6762c46ac550'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('vote', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('votes', 'vote')
    # ### end Alembic commands ###
