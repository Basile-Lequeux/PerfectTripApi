"""Revert userPost

Revision ID: d4e314ed8518
Revises: f52a515bf0b5
Create Date: 2022-03-24 11:38:29.187174

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd4e314ed8518'
down_revision = 'f52a515bf0b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userPost')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userPost',
    sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='userPost_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='userPost_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', 'post_id', name='userPost_pkey')
    )
    # ### end Alembic commands ###