"""empty message

Revision ID: 95e80241642e
Revises: 6d26d6191101
Create Date: 2023-12-20 21:42:47.380712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e80241642e'
down_revision = '6d26d6191101'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.Column('useful', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    # ### end Alembic commands ###