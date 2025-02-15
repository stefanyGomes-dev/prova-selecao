from fastapi import FastAPI, Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
import repositories

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Repository Empresa
empresa_router = APIRouter(prefix="/empresas", tags=["Empresas v1"])

@empresa_router.post(
    "",
    summary="Cria uma nova empresa",
    description="Esta rota permite criar uma nova empresa no banco de dados. O corpo da requisição deve conter os dados da empresa no formato especificado pelo schema `Empresa`.",
    response_description="Retorna os dados da empresa criada.",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Empresa
)
def create_empresa(empresa: schemas.Empresa, db: Session = Depends(get_db)):
    db_empresa = repositories.create_empresa(db, empresa)
    return db_empresa

@empresa_router.get(
    "/{empresa_id}",
    summary="Obtém os dados de uma empresa",
    description="Esta rota retorna os dados de uma empresa específica, identificada pelo `empresa_id`.",
    response_description="Retorna os dados da empresa encontrada.",
    status_code=status.HTTP_200_OK,
    response_model=schemas.EmpresaRead
)
def read_empresa(empresa_id: str, db: Session = Depends(get_db)):
    db_empresa = repositories.get_empresa(db, empresa_id)
    if db_empresa is not None:
        return db_empresa
    else:
        raise HTTPException(status_code=400, detail="Empresa não encontrada")

@empresa_router.delete(
    "/{empresa_id}",
    summary="Remove uma empresa",
    description="Esta rota remove uma empresa específica, identificada pelo `empresa_id`.",
    response_description="Nenhum conteúdo é retornado.",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_empresa(empresa_id: str, db: Session = Depends(get_db)):
    empresa = repositories.get_empresa(db, empresa_id)
    if empresa is not None:
        db.delete(empresa)
        db.commit()
        return
    else:
        raise HTTPException(status_code=400, detail="Empresa não encontrada")

@empresa_router.put(
    "/{empresa_id}",
    summary="Atualiza os dados de uma empresa",
    description="Esta rota permite atualizar os dados de uma empresa existente, identificada pelo `empresa_id`. O corpo da requisição deve conter os campos a serem atualizados no formato especificado pelo schema `EmpresaPatch`.",
    response_description="Retorna os dados atualizados da empresa.",
    status_code=status.HTTP_200_OK,
    response_model=schemas.EmpresaRead
)
def update_empresa(empresa_id: str, update_empresa: schemas.EmpresaPatch, db: Session = Depends(get_db)):
    empresa = repositories.get_empresa(db, empresa_id)
    if empresa is not None:
        repositories.update_empresa(db, update_empresa, empresa_id)
        db.commit()
        db.refresh(empresa)
        return empresa
    else:
        raise HTTPException(status_code=400, detail="Empresa não encontrada")

# Repository Obrigação Acessória
obrigacao_acessoria_router = APIRouter(prefix="/obrigacaoAcessoria", tags=["Obrigacao Acessoria v1"])

@obrigacao_acessoria_router.post(
    "",
    summary="Cria uma nova obrigação acessória",
    description="Esta rota permite criar uma nova obrigação acessória no banco de dados. O corpo da requisição deve conter os dados da obrigação acessória no formato especificado pelo schema `ObrigacaoAcessoria`.",
    response_description="Retorna os dados da obrigação acessória criada.",
    status_code=status.HTTP_201_CREATED
)
def create_obrigacao_acessoria(obrigacao_acessoria: schemas.ObrigacaoAcessoria, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = repositories.create_obrigacao_acessoria(db, obrigacao_acessoria)
    return db_obrigacao_acessoria

@obrigacao_acessoria_router.get(
    "/{obrigacao_acessoria_id}",
    summary="Obtém os dados de uma obrigação acessória",
    description="Esta rota retorna os dados de uma obrigação acessória específica, identificada pelo `obrigacao_acessoria_id`.",
    response_description="Retorna os dados da obrigação acessória encontrada.",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ObrigacaoAcessoriaRead
)
def read_obrigacao_acessoria(obrigacao_acessoria_id: str, db: Session = Depends(get_db)):
    db_obrigacao_acessoria = repositories.get_obrigacao_acessoria(db, obrigacao_acessoria_id)
    return db_obrigacao_acessoria

@obrigacao_acessoria_router.delete(
    "/{obrigacao_acessoria_id}",
    summary="Remove uma obrigação acessória",
    description="Esta rota remove uma obrigação acessória específica, identificada pelo `obrigacao_acessoria_id`.",
    response_description="Nenhum conteúdo é retornado.",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_obrigacao_acessoria(obrigacao_acessoria_id: str, db: Session = Depends(get_db)):
    obrigacao_acessoria = repositories.get_obrigacao_acessoria(db, obrigacao_acessoria_id)
    if obrigacao_acessoria is not None:
        db.delete(obrigacao_acessoria)
        db.commit()
        return
    else:
        raise HTTPException(status_code=400, detail="Obrigação Acessória não encontrada")

@obrigacao_acessoria_router.put(
    "/{obrigacao_acessoria_id}",
    summary="Atualiza os dados de uma obrigação acessória",
    description="Esta rota permite atualizar os dados de uma obrigação acessória existente, identificada pelo `obrigacao_acessoria_id`. O corpo da requisição deve conter os campos a serem atualizados no formato especificado pelo schema `ObrigacaoAcessoriaPatch`.",
    response_description="Retorna os dados atualizados da obrigação acessória.",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ObrigacaoAcessoriaRead
)
def update_obrigacao_acessoria(obrigacao_acessoria_id: str, update_obrigacao_acessoria: schemas.ObrigacaoAcessoriaPatch, db: Session = Depends(get_db)):
    obrigacao_acessoria = repositories.get_obrigacao_acessoria(db, obrigacao_acessoria_id)
    if obrigacao_acessoria is not None:
        repositories.update_obrigacao_acessoria(db, update_obrigacao_acessoria, obrigacao_acessoria_id)
        db.commit()
        db.refresh(obrigacao_acessoria)
        return obrigacao_acessoria
    else:
        raise HTTPException(status_code=400, detail="Obrigação Acessória não encontrada")

app.include_router(empresa_router, prefix="/v1")
app.include_router(obrigacao_acessoria_router, prefix="/v1")