"""Create wallets table

Revision ID: 001
Revises: 
Create Date: 2025-11-17 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('wallets',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('balance', sa.Numeric(precision=20, scale=2), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('wallets')