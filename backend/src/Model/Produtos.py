from pydantic import BaseModel

class Produto(BaseModel):
    categoria_produto:str
    nome_produto:str
    marca_produto:str
    modelo_produto:str
    cor_produto:str
    numero_serie:str
    status_produto:str
    desc_produto:str | None = None
    quantidade:int
    valor:float

class Estoque(BaseModel):
    produto:Produto
    quantidade:int
    valor:float
    data_entrada:str
    obs_entrada:str | None = None
    data_saida:str | None = None
    obs_saida:str | None = None
    status_entrada:str
    status_saida:str | None = None
    valor_total:float

class Aparelho(BaseModel):
    nome_aparelho:str
    desc_aparelho:str | None = None
    marca_aparelho:str
    modelo_aparelho:str
    cor_aparelho:str
    numero_serie:str
    status_aparelho:str
    obs_aparelho:str | None = None
