"""empty message

Revision ID: 6a4910ea4d19
Revises: 11caedebde14
Create Date: 2020-04-15 23:08:06.941064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a4910ea4d19'
down_revision = '11caedebde14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_profiles_email_key', 'user_profiles', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_profiles_email_key', 'user_profiles', ['email'])
    # ### end Alembic commands ###
