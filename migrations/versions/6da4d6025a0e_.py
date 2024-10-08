"""empty message

Revision ID: 6da4d6025a0e
Revises: 
Create Date: 2024-09-14 18:37:31.106961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6da4d6025a0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('capitais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('regiao', sa.String(length=100), nullable=True),
    sa.Column('estado', sa.String(length=100), nullable=True),
    sa.Column('sigla', sa.String(length=100), nullable=True),
    sa.Column('capital', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('capitais')
    # ### end Alembic commands ###
