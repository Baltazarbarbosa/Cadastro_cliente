from fastapi import FastAPI
from Model.Pessoa import Pessoa
from Model.Produtos import Produto
from bd.postgresManager import PostgresManager
from Dao.persistirDados import inserirCliente, inserirProduto
from fastapi.responses import Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/inserirCliente")
async def inserirClientes(cliente: Pessoa, response: Response):
    try:
        print(cliente)
        pg = PostgresManager.getInstance()
        print(pg)
        retorno = inserirCliente(pg,cliente)

        if retorno["status"]:
            response.status_code = 200
            return {
                "status": True,
                "message": "Cliente cadastrado com sucesso!"
            }
        else:
            response.status_code = 400
            return {
                "status": False,
                "message": "Erro ao cadastrar cliente!"
            }
        
        
    except Exception as error:
        print(error)
        raise error    

@app.post("/inserirProduto")
async def inserirProdutos(produto: Produto, response: Response):
    try:
        print(produto)
        pg = PostgresManager.getInstance()
        print(pg)
        retorno = inserirProduto(pg,produto)

        if retorno["status"]:
            response.status_code = 200
            return {
                "status": True,
                "message": "Produto cadastrado com sucesso!"
            }
        else:
            response.status_code = 400
            return {
                "status": False,
                "message": "Erro ao cadastrar produto!"
            }
        
        
    except Exception as error:
        print(error)
        raise error