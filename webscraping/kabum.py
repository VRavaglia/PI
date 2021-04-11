kabum_base = 'https://www.kabum.com.br/'
kabum_mobo = kabum_base + 'hardware/placas-mae?pagina=1&ordem=5&limite=1000&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'

from urllib.request import urlopen
from bs4 import BeautifulSoup
from enum import Enum
import json

DEBUG = True

def listar_todos_por_tipo(tipo):
    url = {'mobo' : kabum_mobo}

    arquivo_debug = tipo + "debug.html"
    
    if not DEBUG:
        html = urlopen(url[tipo])
        bs = BeautifulSoup(html, 'html.parser')
        f = open(arquivo_debug, "w")
        f.write(bs.prettify())
        f.close()
        
    # o arquivo html local esta sempre sendo criado
    # idealmente apenas se em debug o arquivo seria criado

    f = open(arquivo_debug, "r") 
    linhas = f.readlines()
    f.close()

    dados_str = ''

    for linha in linhas:
        pos = linha.find("listagemDados")
        if pos != -1: 
            dados_str = linha[30:]
    
    dados = json.loads(dados_str)

    produtos = []

    for produto in dados:
        produtos.append({'nome': produto['nome'],'preco': produto['preco'], 'preco_desconto': produto['preco_desconto'], 'link': produto['link_descricao']})

    return produtos