"""init

Revision ID: 11f1e940695e
Revises: 
Create Date: 2019-02-02 22:05:33.689016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11f1e940695e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('horses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('str', sa.Integer(), nullable=False),
    sa.Column('active', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_horses')),
    sa.UniqueConstraint('name', name=op.f('uq_horses_name'))
    )
    op.create_table('races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('race_number', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('place', sa.Integer(), nullable=True),
    sa.Column('horse_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['horse_id'], ['horses.id'], name=op.f('fk_races_horse_id_horses')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_races'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('races')
    op.drop_table('horses')
    # ### end Alembic commands ###
