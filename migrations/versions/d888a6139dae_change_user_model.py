"""change user model

Revision ID: d888a6139dae
Revises: afd106a1fdf7
Create Date: 2017-05-25 21:59:17.111704

"""

# revision identifiers, used by Alembic.
revision = 'd888a6139dae'
down_revision = 'afd106a1fdf7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(u'ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_users_email', table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###