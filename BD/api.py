from classesProdutos import *
import sqlite3
from datetime import datetime
import sys
sys.path.append('../InfoExt')
sys.path.append('../webscraping')
from manager import manageProd, checker
from mainWebscraping import listar_todos_por_tipo
from pprint import pprint

database = 'main.sqlite'
tipos = ['mobo', 'psu', 'ram', 'cpu', 'gpu', 'case', 'hd']

def getChaves(produto):
    chaves = [a for a in dir(produto) if (not a.startswith('__') and a != 'tipo' and a != 'info_adicionais'and a != 'parametros' and a != 'info_ad' and a != 'updater')]
    # print(chaves)
    return chaves

def class2val(produto):
    chaves = getChaves(produto)

    #print(produto.nome)

    valores = ''

    for chave in chaves:
        valor = produto.__dict__[chave]

     #   print(chave)
      #  print(valor)

        if type(valor) is int or type(valor) is float:
            valores = valores + ', ' + str(valor)
        else:
            valores = valores + ', \'' + valor + '\''
    
    valores = valores[2:]
    return valores

def class2chave(produto):
    chaves = getChaves(produto)

    chavesStr = ''

    for chave in chaves:
        chavesStr = chavesStr + ', ' + chave

    chavesStr = chavesStr[2:]

    return chavesStr


def inserirProduto(produto):
    con = sqlite3.connect(database)
    cur = con.cursor()

    valores = class2val(produto)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    valores = '(' + valores + ', \'' + data + '\'' +')'

    chaves = class2chave(produto)
    chaves = '(' + chaves + ', data)'

    insercao = "INSERT INTO " + produto.tipo + " " + chaves +" VALUES " + valores

    #print(insercao)

    cur.execute(insercao)

    con.commit()
    con.close()

def inserirTodos():
    loja = 'kabum'
    for tipo in tipos:
        produtos = listar_todos_por_tipo(loja, tipo)
        produtos_classificados = list()
        manageProd(produtos, (tipo, produtos_classificados))
        checker((tipo, produtos_classificados))

        for produto in produtos_classificados:
            try:
                inserirProduto(produto)
            except:
                print("Erro na inserção")
                print(produto.nome)
                print(produto.__dict__)
                input("Pressione uma tecla para continuar...")

def deletarTodos():
    con = sqlite3.connect(database)
    cur = con.cursor()

    for tipo in tipos:
        # print(tipo)
        cur.execute("DELETE from \"" + tipo + "\"")

    con.commit()
    con.close()