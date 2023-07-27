import sqlalchemy
from Model.Pessoa import Pessoa
from Model.Produtos import Produto
import sqlalchemy
from bd.postgresql import Postgres

def inserirCliente(pg:Postgres, Cliente:Pessoa):
  try:
    pg.connect()
    conpg = pg.getConnection()
    
    query = """INSERT INTO public.clientes
                (nome, cpf, rg, email, rua, numero, complemento, bairro, cidade, cep, tipo_telefone, ddd, numero_telefone)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
                """.format(Cliente.nome,
                           Cliente.cpf,
                           Cliente.rg,
                           Cliente.email,
                           Cliente.endereco_pessoa.rua,
                           Cliente.endereco_pessoa.numero,
                           Cliente.endereco_pessoa.complemento,
                           Cliente.endereco_pessoa.bairro,
                           Cliente.endereco_pessoa.cidade,
                           Cliente.endereco_pessoa.cep,
                           Cliente.telefone_pessoa.tipo_telefone,
                           Cliente.telefone_pessoa.ddd,
                           Cliente.telefone_pessoa.numero)
    
    trans = conpg.begin()
    query_nova = sqlalchemy.text(query)
    results = conpg.execute(query_nova)
    if results.rowcount > 0:
      trans.commit()
      return {
        "status": True
      } 
    else:
      trans.rollback()
      return {
        "status": False
      }
  except Exception as error:
    raise error
  
def inserirProduto(pg:Postgres, Produto:Produto):
  try:
    pg.connect()
    conpg = pg.getConnection()
    query = """
              insert into produto(categoria_produto,nome_produto,desc_produto,quantidade,valor) 
                          values ('{}','{}','{}',{},{})""".format(Produto.categoria_produto,
                                                                      Produto.nome_produto,
                                                                      Produto.desc_produto,
                                                                      Produto.quantidade,
                                                                      Produto.valor)
    trans = conpg.begin()
    query_nova = sqlalchemy.text(query)
    results = conpg.execute(query_nova)
    if results.rowcount > 0:
      trans.commit()
      return {
        "status": True
      } 
    else:
      trans.rollback()
      return {
        "status": False
      }
  except Exception as error:
    raise error