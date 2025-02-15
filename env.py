import os
from models import Empresa, ObrigacaoAcessoria
from logging.config import fileConfig
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from alembic import context


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Leia o arquivo de configuração alembic.ini
fileConfig('alembic.ini')

# Obter variáveis do .env
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SCHEMA = os.getenv("DB_SCHEMA")

# Construir a URL de conexão PostgreSQL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?schema={DB_SCHEMA}"

# Criar o engine com a URL do banco
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Chame a função que executa as migrações
def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,  # Usando a URL construída
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine.connect()

    with connectable.begin():
        context.configure(
            connection=connectable,
            target_metadata=Base.metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# Escolha o modo de migração (online ou offline)
def run():
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()

if __name__ == "__main__":
    run()
