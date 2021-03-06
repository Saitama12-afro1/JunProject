"""Initial migration

Revision ID: e34dd31adbb8
Revises: d4d95d35612a
Create Date: 2022-05-05 14:26:31.447166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e34dd31adbb8'
down_revision = 'd4d95d35612a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    sa.UniqueConstraint('username', name='users_username_key')
    )
    op.create_table('questions',
    sa.Column('id_question', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text_question', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('text_answer', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_question', name='questions_pkey'),
    sa.UniqueConstraint('text_question', name='questions_text_question_key')
    )
    # ### end Alembic commands ###
