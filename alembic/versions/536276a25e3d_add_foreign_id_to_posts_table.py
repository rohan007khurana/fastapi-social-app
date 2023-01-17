"""add foreign id to posts table

Revision ID: 536276a25e3d
Revises: 51198e4cb814
Create Date: 2023-01-17 11:28:31.611566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536276a25e3d'
down_revision = '51198e4cb814'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
