from fastapi.testclient import TestClient
from main import app, get_db
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaRead, ObrigacaoAcessoriaRead

# Cria o cliente de teste
client = TestClient(app)

# Mock da sessão do banco de dados
mock_db = MagicMock(spec=Session)

# Sobrescreve a dependência get_db para usar o mock
app.dependency_overrides[get_db] = lambda: mock_db

# Testes para Empresa
def test_create_empresa():
    # Dados da empresa
    empresa_data = {
        "nome": "Empresa Teste",
        "cnpj": "12345678901234",
        "endereco": "Rua Teste, 123",
        "email": "teste@empresa.com",
        "telefone": "11987654321"
    }

    # Mock do retorno do repositório
    mock_db.query.return_value.filter.return_value.first.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    # Chama o endpoint
    response = client.post("/v1/empresas", json=empresa_data)

    # Verifica a resposta
    assert response.status_code == 201
    assert response.json()["nome"] == "Empresa Teste"

def test_read_empresa():
    # Mock do retorno do repositório
    mock_empresa = MagicMock()
    mock_empresa.id = 1
    mock_empresa.nome = "Empresa Teste"
    mock_empresa.cnpj = "12345678901234"
    mock_empresa.endereco = "Rua Teste, 123"
    mock_empresa.email = "teste@empresa.com"
    mock_empresa.telefone = "11987654321"

    mock_db.query.return_value.filter.return_value.first.return_value = mock_empresa

    # Chama o endpoint
    response = client.get("/v1/empresas/1")

    # Verifica a resposta
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

def test_update_empresa():
    # Mock do retorno do repositório
    mock_empresa = MagicMock()
    mock_empresa.id = 1
    mock_empresa.nome = "Empresa Teste"
    mock_empresa.cnpj = "12345678901234"
    mock_empresa.endereco = "Rua Teste, 123"
    mock_empresa.email = "teste@empresa.com"
    mock_empresa.telefone = "11987654321"

    mock_db.query.return_value.filter.return_value.first.return_value = mock_empresa
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    # Dados de atualização
    update_data = {"nome": "Empresa Atualizada"}

    # Chama o endpoint
    response = client.put("/v1/empresas/1", json=update_data)

    # Verifica a resposta
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Atualizada"

def test_delete_empresa():
    # Mock do retorno do repositório
    mock_empresa = MagicMock()
    mock_empresa.id = 1
    mock_empresa.nome = "Empresa Teste"
    mock_empresa.cnpj = "12345678901234"
    mock_empresa.endereco = "Rua Teste, 123"
    mock_empresa.email = "teste@empresa.com"
    mock_empresa.telefone = "11987654321"

    mock_db.query.return_value.filter.return_value.first.return_value = mock_empresa
    mock_db.commit.return_value = None
    mock_db.delete.return_value = None

    # Chama o endpoint
    response = client.delete("/v1/empresas/1")

    # Verifica a resposta
    assert response.status_code == 204

    # Verifica se a empresa foi excluída
    mock_db.delete.assert_called_once_with(mock_empresa)

# Testes para ObrigacaoAcessoria
def test_create_obrigacao_acessoria():
    # Dados da obrigação acessória
    obrigacao_data = {
        "nome": "Obrigacao Teste",
        "periodicidade": "Mensal",
        "empresa_id": 1
    }

    # Mock do retorno do repositório
    mock_db.query.return_value.filter.return_value.first.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    # Chama o endpoint
    response = client.post("/v1/obrigacaoAcessoria", json=obrigacao_data)

    # Verifica a resposta
    assert response.status_code == 201
    assert response.json()["nome"] == "Obrigacao Teste"

def test_read_obrigacao_acessoria():
    # Mock do retorno do repositório
    mock_obrigacao = MagicMock()
    mock_obrigacao.id = 1
    mock_obrigacao.nome = "Obrigacao Teste"
    mock_obrigacao.periodicidade = "Mensal"
    mock_obrigacao.empresa_id = 1

    mock_db.query.return_value.filter.return_value.first.return_value = mock_obrigacao

    # Chama o endpoint
    response = client.get("/v1/obrigacaoAcessoria/1")

    # Verifica a resposta
    assert response.status_code == 200
    assert response.json()["nome"] == "Obrigacao Teste"

def test_update_obrigacao_acessoria():
    # Mock do retorno do repositório
    mock_obrigacao = MagicMock()
    mock_obrigacao.id = 1
    mock_obrigacao.nome = "Obrigacao Teste"
    mock_obrigacao.periodicidade = "Mensal"
    mock_obrigacao.empresa_id = 1

    mock_db.query.return_value.filter.return_value.first.return_value = mock_obrigacao
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    # Dados de atualização
    update_data = {"nome": "Obrigacao Atualizada"}

    # Chama o endpoint
    response = client.put("/v1/obrigacaoAcessoria/1", json=update_data)

    # Verifica a resposta
    assert response.status_code == 200
    assert response.json()["nome"] == "Obrigacao Atualizada"

def test_delete_obrigacao_acessoria():
    # Mock do retorno do repositório
    mock_obrigacao = MagicMock()
    mock_obrigacao.id = 1
    mock_obrigacao.nome = "Obrigacao Teste"
    mock_obrigacao.periodicidade = "Mensal"
    mock_obrigacao.empresa_id = 1

    mock_db.query.return_value.filter.return_value.first.return_value = mock_obrigacao
    mock_db.commit.return_value = None
    mock_db.delete.return_value = None

    # Chama o endpoint
    response = client.delete("/v1/obrigacaoAcessoria/1")

    # Verifica a resposta
    assert response.status_code == 204