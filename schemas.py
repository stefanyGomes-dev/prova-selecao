from pydantic import BaseModel, ConfigDict
from typing import Optional


class Empresa(BaseModel):
    nome : str
    cnpj : str
    endereco : str
    email : str
    telefone : str


class EmpresaRead(Empresa):
    id : int

    model_config = ConfigDict(from_attributes=True)


class EmpresaPatch(BaseModel):
    nome : Optional[str] = None
    cnpj : Optional[str] = None
    endereco : Optional[str] = None
    email : Optional[str] = None
    telefone : Optional[str] = None


class EmpresaDelete(BaseModel):
    id : int


class ObrigacaoAcessoria(BaseModel):
    nome : str
    periodicidade : str
    empresa_id : int


class ObrigacaoAcessoriaRead(ObrigacaoAcessoria):
    id : int

    model_config = ConfigDict(from_attributes=True)


class ObrigacaoAcessoriaPatch(BaseModel):
    nome : Optional[str] = None
    periodicidade : Optional[str] = None


class ObrigacaoAcessoriaDelete(BaseModel):
    id : int