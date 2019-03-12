"""field change

Revision ID: 0fbdc69426a4
Revises: 6ca3a859af6c
Create Date: 2019-03-01 16:29:47.295676

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0fbdc69426a4'
down_revision = '6ca3a859af6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uploadimg', 'src',
               existing_type=mysql.VARCHAR(length=64),
               type_=sa.String(length=600),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('uploadimg', 'src',
               existing_type=sa.String(length=600),
               type_=mysql.VARCHAR(length=64),
               existing_nullable=True)
    # ### end Alembic commands ###