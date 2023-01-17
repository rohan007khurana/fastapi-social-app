"""create users table

Revision ID: 51198e4cb814
Revises: 9688181f2b2f
Create Date: 2023-01-17 11:24:25.847236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51198e4cb814'
down_revision = '9688181f2b2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
