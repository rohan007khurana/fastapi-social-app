"""create vote table

Revision ID: 463725a7fa1a
Revises: 536276a25e3d
Create Date: 2023-01-17 11:29:51.073205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '463725a7fa1a'
down_revision = '536276a25e3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
