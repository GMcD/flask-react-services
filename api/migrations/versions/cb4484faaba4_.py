"""empty message

Revision ID: cb4484faaba4
Revises: 
Create Date: 2020-09-01 20:44:46.592404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb4484faaba4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reflask_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('reflask_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password_hash'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_reflask_users_email'), 'reflask_users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reflask_users_email'), table_name='reflask_users')
    op.drop_table('reflask_users')
    op.drop_table('reflask_posts')
    # ### end Alembic commands ###
