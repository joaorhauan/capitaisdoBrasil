"""empty message

Revision ID: d06f26493a7b
Revises: 6da4d6025a0e
Create Date: 2024-09-14 18:42:23.629363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd06f26493a7b'
down_revision = '6da4d6025a0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_usuario', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'usuario', ['id_usuario'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diario', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_usuario')

    # ### end Alembic commands ###
