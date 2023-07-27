from pydantic import BaseModel

class Endereco(BaseModel):
    rua:str | None = None
    numero:str | None = None
    complemento:str | None = None
    bairro:str | None = None
    cidade:str | None = None
    cep:str | None = None

class Telefone(BaseModel):
    tipo_telefone:str
    ddd:str
    numero:str

class Pessoa(BaseModel):
   
    nome:str
    cpf:str
    rg:str | None = None
    email:str | None = None
    endereco_pessoa:Endereco | None = None
    telefone_pessoa:Telefone

