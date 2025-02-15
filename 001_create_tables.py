from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


def upgrade():
    op.create_table(
        'empresas',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('nome', sa.String, nullable=False),
        sa.Column('cnpj', sa.String, unique=True, nullable=False),
        sa.Column('endereco', sa.String),
        sa.Column('email', sa.String),
        sa.Column('telefone', sa.String),
    )

    
    op.create_table(
        'obrigacoes_acessorias',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('nome', sa.String, nullable=False),
        sa.Column('periodicidade', sa.String),
        sa.Column('empresa_id', sa.Integer, sa.ForeignKey('empresas.id')),
    )

def downgrade():
    
    op.drop_table('obrigacoes_acessorias')
    op.drop_table('empresas')
