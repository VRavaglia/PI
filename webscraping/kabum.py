kabum_base = 'https://www.kabum.com.br/'
kabum_mobo = kabum_base + 'hardware/placas-mae?pagina=1&ordem=5&limite=1000&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_psu = kabum_base + 'hardware/fontes?pagina=1&ordem=5&limite=1000&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_ram = kabum_base + 'hardware/memoria-ram?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_cpu = kabum_base + 'hardware/processadores?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_gpu = kabum_base + 'hardware/placa-de-video-vga?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_case = kabum_base + 'perifericos/gabinetes?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_cooler = kabum_base + 'hardware/coolers?pagina=1&ordem=5&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'

from urllib.request import urlopen
from bs4 import BeautifulSoup
from enum import Enum
import json

DEBUG = True

def listar_todos_por_tipo(tipo):
    url = {'mobo' : kabum_mobo, 'psu' : kabum_psu, 'ram' : kabum_ram, 'cpu' : kabum_cpu, 'gpu' : kabum_gpu, 'case' : kabum_case, 'cooler': kabum_cooler}

    arquivo_debug = "kb_" + tipo + "_debug.html"
    
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

    arquivo_parseado = "kb_" + tipo + "_parseado.txt"
    f = open(arquivo_parseado, "w") 

    for produto in dados:
        produtos.append({'nome': produto['nome'],'preco': produto['preco'], 'preco_desconto': produto['preco_desconto'], 'link': produto['link_descricao']})

    f.write(str(produtos))
    f.close()

    return produtos