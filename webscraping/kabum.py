kabum_base = 'https://www.kabum.com.br/'
kabum_end = '&ordem=3&limite=100&prime=false&marcas=[]&tipo_produto=[]&filtro=[]'
kabum_pg = 'pagina='
kabum_mobo = kabum_base + 'hardware/placas-mae?'
kabum_psu = kabum_base + 'hardware/fontes?'
kabum_ram = kabum_base + 'hardware/memoria-ram?'
kabum_cpu = kabum_base + 'hardware/processadores?'
kabum_gpu = kabum_base + 'hardware/placa-de-video-vga?'
kabum_case = kabum_base + 'perifericos/gabinetes?'
kabum_cooler = kabum_base + 'hardware/coolers?'
kabum_hd = kabum_base + 'hardware/disco-rigido-hd?'
kabum_ssd = kabum_base + 'hardware/ssd-2-5?'

prod_skip = 30

from urllib.request import urlopen
from bs4 import BeautifulSoup
from enum import Enum
from pprint import pprint
import os
import json

DEBUG = True

def listar_todos_por_tipo(tipo):
    url_produto = {'mobo' : kabum_mobo, 'psu' : kabum_psu, 'ram' : kabum_ram, 'cpu' : kabum_cpu, 'gpu' : kabum_gpu, 'case' : kabum_case, 'cooler': kabum_cooler, 'hd': kabum_hd, 'ssd': kabum_ssd}

    
    continuar = True
    pagina = 0
    produtos = []
    cnt_pronduto = 0

    while continuar:
        pagina = pagina + 1
        arquivo_debug = "../webscraping/" + "kb_" + tipo +'_' + str(pagina) +"_debug.html"

        if not DEBUG:
            
            
            url = url_produto[tipo] + kabum_pg + str(pagina) + kabum_end

            html = urlopen(url)
            bs = BeautifulSoup(html, 'html.parser')
            f = open(arquivo_debug, "w")
            f.write(bs.prettify())
            f.close()
            
        # o arquivo html local esta sempre sendo criado
        # idealmente apenas se em debug o arquivo seria criado

        f = open(arquivo_debug, "r", encoding='latin-1') 
        linhas = f.readlines()
        f.close()

        dados_str = ''

        for linha in linhas:
            pos = linha.find("listagemDados")
            if pos != -1: 
                dados_str = linha[30:]
        
        dados = json.loads(dados_str)

        arquivo_parseado = "kb_" + tipo + "_parseado.txt"
        f = open(arquivo_parseado, "w") 

        if len(dados) < 100:
            continuar = False
            print("Fim das paginas")

        preco_anterior = 0
        prod_anterior = []

        for produto in dados:
            cnt_pronduto = cnt_pronduto + 1
            if produto['disponibilidade']:
                produtos.append({'nome': produto['nome'],'preco': produto['preco'], 'preco_desconto': produto['preco_desconto'], 'link': produto['link_descricao'], 'site': 'kabum.com.br'})

        f.write(str(produtos))
        f.close()

    # idx_max = -1
    # idx = -1
    # preco_max = -1

    # for produto in produtos:
    #     print(produto['preco_desconto'])
    #     idx = idx + 1

    #     if produto['preco_desconto'] >= preco_max:
    #         preco_max = produto['preco_desconto']
    #         idx_max = idx
    
    # print(produtos[idx_max], idx_max)

    # produtos = produtos[0:idx_max+1]

    return produtos
