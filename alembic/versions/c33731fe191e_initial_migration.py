"""Initial migration

Revision ID: c33731fe191e
Revises: 
Create Date: 2024-06-22 00:38:40.478930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c33731fe191e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_addresses_city'), 'addresses', ['city'], unique=False)
    op.create_index(op.f('ix_addresses_country'), 'addresses', ['country'], unique=False)
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=False)
    op.create_index(op.f('ix_addresses_postal_code'), 'addresses', ['postal_code'], unique=False)
    op.create_index(op.f('ix_addresses_state'), 'addresses', ['state'], unique=False)
    op.create_index(op.f('ix_addresses_street'), 'addresses', ['street'], unique=False)
    op.create_table('companies',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('register_number', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companies_email'), 'companies', ['email'], unique=False)
    op.create_index(op.f('ix_companies_id'), 'companies', ['id'], unique=False)
    op.create_index(op.f('ix_companies_name'), 'companies', ['name'], unique=False)
    op.create_index(op.f('ix_companies_phone'), 'companies', ['phone'], unique=False)
    op.create_index(op.f('ix_companies_postal_code'), 'companies', ['postal_code'], unique=False)
    op.create_index(op.f('ix_companies_register_number'), 'companies', ['register_number'], unique=True)
    op.create_table('shipments',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('company_id', sa.String(), nullable=True),
    sa.Column('contract_id', sa.String(), nullable=True),
    sa.Column('order_number', sa.String(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('shipment_type', sa.String(), nullable=True),
    sa.Column('origin_street', sa.String(), nullable=True),
    sa.Column('origin_city', sa.String(), nullable=True),
    sa.Column('origin_state', sa.String(), nullable=True),
    sa.Column('origin_postal_code', sa.String(), nullable=True),
    sa.Column('destination_name', sa.String(), nullable=True),
    sa.Column('destination_street', sa.String(), nullable=True),
    sa.Column('destination_city', sa.String(), nullable=True),
    sa.Column('destination_state', sa.String(), nullable=True),
    sa.Column('destination_postal_code', sa.String(), nullable=True),
    sa.Column('destination_phone', sa.String(), nullable=True),
    sa.Column('destination_email', sa.String(), nullable=True),
    sa.Column('ship_date', sa.DateTime(), nullable=True),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.Column('delivery_status', sa.String(), nullable=True),
    sa.Column('estimated_shipment_date', sa.DateTime(), nullable=True),
    sa.Column('estimated_delivery_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shipments_company_id'), 'shipments', ['company_id'], unique=False)
    op.create_index(op.f('ix_shipments_contract_id'), 'shipments', ['contract_id'], unique=False)
    op.create_index(op.f('ix_shipments_delivery_status'), 'shipments', ['delivery_status'], unique=False)
    op.create_index(op.f('ix_shipments_destination_city'), 'shipments', ['destination_city'], unique=False)
    op.create_index(op.f('ix_shipments_destination_email'), 'shipments', ['destination_email'], unique=False)
    op.create_index(op.f('ix_shipments_destination_name'), 'shipments', ['destination_name'], unique=False)
    op.create_index(op.f('ix_shipments_destination_phone'), 'shipments', ['destination_phone'], unique=False)
    op.create_index(op.f('ix_shipments_destination_postal_code'), 'shipments', ['destination_postal_code'], unique=False)
    op.create_index(op.f('ix_shipments_destination_state'), 'shipments', ['destination_state'], unique=False)
    op.create_index(op.f('ix_shipments_destination_street'), 'shipments', ['destination_street'], unique=False)
    op.create_index(op.f('ix_shipments_id'), 'shipments', ['id'], unique=False)
    op.create_index(op.f('ix_shipments_order_number'), 'shipments', ['order_number'], unique=False)
    op.create_index(op.f('ix_shipments_origin_postal_code'), 'shipments', ['origin_postal_code'], unique=False)
    op.create_table('contracts',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('company_id', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contracts_company_id'), 'contracts', ['company_id'], unique=False)
    op.create_index(op.f('ix_contracts_id'), 'contracts', ['id'], unique=False)
    op.create_index(op.f('ix_contracts_start_date'), 'contracts', ['start_date'], unique=False)
    op.create_table('postal_code_ranges',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('contract_id', sa.String(), nullable=True),
    sa.Column('start_postal_code', sa.String(), nullable=False),
    sa.Column('end_postal_code', sa.String(), nullable=False),
    sa.Column('delivery_rate_per_kg', sa.Float(), nullable=False),
    sa.Column('delivery_rate_per_volume', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['contract_id'], ['contracts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_postal_code_ranges_contract_id'), 'postal_code_ranges', ['contract_id'], unique=False)
    op.create_index(op.f('ix_postal_code_ranges_end_postal_code'), 'postal_code_ranges', ['end_postal_code'], unique=False)
    op.create_index(op.f('ix_postal_code_ranges_id'), 'postal_code_ranges', ['id'], unique=False)
    op.create_index(op.f('ix_postal_code_ranges_start_postal_code'), 'postal_code_ranges', ['start_postal_code'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_postal_code_ranges_start_postal_code'), table_name='postal_code_ranges')
    op.drop_index(op.f('ix_postal_code_ranges_id'), table_name='postal_code_ranges')
    op.drop_index(op.f('ix_postal_code_ranges_end_postal_code'), table_name='postal_code_ranges')
    op.drop_index(op.f('ix_postal_code_ranges_contract_id'), table_name='postal_code_ranges')
    op.drop_table('postal_code_ranges')
    op.drop_index(op.f('ix_contracts_start_date'), table_name='contracts')
    op.drop_index(op.f('ix_contracts_id'), table_name='contracts')
    op.drop_index(op.f('ix_contracts_company_id'), table_name='contracts')
    op.drop_table('contracts')
    op.drop_index(op.f('ix_shipments_origin_postal_code'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_order_number'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_id'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_street'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_state'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_postal_code'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_phone'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_name'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_email'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_destination_city'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_delivery_status'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_contract_id'), table_name='shipments')
    op.drop_index(op.f('ix_shipments_company_id'), table_name='shipments')
    op.drop_table('shipments')
    op.drop_index(op.f('ix_companies_register_number'), table_name='companies')
    op.drop_index(op.f('ix_companies_postal_code'), table_name='companies')
    op.drop_index(op.f('ix_companies_phone'), table_name='companies')
    op.drop_index(op.f('ix_companies_name'), table_name='companies')
    op.drop_index(op.f('ix_companies_id'), table_name='companies')
    op.drop_index(op.f('ix_companies_email'), table_name='companies')
    op.drop_table('companies')
    op.drop_index(op.f('ix_addresses_street'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_state'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_postal_code'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_country'), table_name='addresses')
    op.drop_index(op.f('ix_addresses_city'), table_name='addresses')
    op.drop_table('addresses')
    # ### end Alembic commands ###
