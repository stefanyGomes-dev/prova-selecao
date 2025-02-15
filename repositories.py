import models, schemas
from sqlalchemy.orm import Session


# Empresas

def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()


def create_empresa(db: Session, empresa: schemas.Empresa):
    db_empresa = models.Empresa(nome = empresa.nome,
                             cnpj = empresa.cnpj,
                             endereco = empresa.endereco,
                             email = empresa.email,
                             telefone = empresa.telefone)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa


def delete_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).delete()



def update_empresa(db: Session, update_empresa: models.Empresa, empresa_id: int):
    empresa = get_empresa(db, empresa_id)

    if empresa is not None:        
        empresa.nome = update_empresa.nome if update_empresa.nome != None else empresa.nome
        empresa.cnpj = update_empresa.cnpj if update_empresa.cnpj != None else empresa.cnpj
        empresa.endereco = update_empresa.endereco if update_empresa.endereco != None else empresa.endereco
        empresa.email = update_empresa.email if update_empresa.email != None else empresa.email
        empresa.telefone = update_empresa.telefone if update_empresa.telefone != None else empresa.telefone
        
        db.commit()
        db.refresh(empresa)        
        return empresa
    else:
        return None


# Obrigação Acessória

def get_obrigacao_acessoria(db: Session, obrigacao_acessoria_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_acessoria_id).first()


def create_obrigacao_acessoria(db: Session, obrigacao_acessoria: schemas.ObrigacaoAcessoria):
    db_obrigacao_acessoria = models.ObrigacaoAcessoria(nome = obrigacao_acessoria.nome,
                                           periodicidade = obrigacao_acessoria.periodicidade,
                                           empresa_id = obrigacao_acessoria.empresa_id)
    db.add(db_obrigacao_acessoria)
    db.commit()
    db.refresh(db_obrigacao_acessoria)

    return db_obrigacao_acessoria


def delete_obrigacao_acessoria(db: Session, obrigacao_acessoria_id: int):
    return db.query(models.ObrigacaoAcessoria).filter(models.ObrigacaoAcessoria.id == obrigacao_acessoria_id).delete()


def update_obrigacao_acessoria(db: Session, update_obrigacao_acessoria: models.ObrigacaoAcessoria, obrigacao_acessoria_id: int):
    obrigacao_acessoria = get_obrigacao_acessoria(db, obrigacao_acessoria_id)

    if obrigacao_acessoria is not None:
        print(update_obrigacao_acessoria.nome)        
        obrigacao_acessoria.nome = update_obrigacao_acessoria.nome if update_obrigacao_acessoria.nome != None else obrigacao_acessoria.nome

        obrigacao_acessoria.periodicidade = update_obrigacao_acessoria.periodicidade if update_obrigacao_acessoria.periodicidade != None else obrigacao_acessoria.periodicidade

        db.commit()
        db.refresh(obrigacao_acessoria)        
        return obrigacao_acessoria
    else:
        return None