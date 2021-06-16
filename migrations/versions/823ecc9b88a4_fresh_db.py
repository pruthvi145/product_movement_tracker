"""fresh db

Revision ID: 823ecc9b88a4
Revises: 
Create Date: 2021-06-16 13:01:25.056648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '823ecc9b88a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_movement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('from_location_id', sa.Integer(), nullable=True),
    sa.Column('to_location_id', sa.Integer(), nullable=True),
    sa.Column('timestemp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['from_location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['to_location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_movement')
    op.drop_table('product')
    op.drop_table('location')
    # ### end Alembic commands ###