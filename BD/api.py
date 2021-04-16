from classesProdutos import *
import sqlite3
from datetime import datetime

database = 'main.sqlite'

def getChaves(produto):
    chaves = [a for a in dir(produto) if (not a.startswith('__') and a != 'tipo' and a != 'info_adicionais'and a != 'parametros' and a != 'info_ad')]
    print(chaves)
    return chaves

def class2val(produto):
    chaves = getChaves(produto)

    valores = ''

    for chave in chaves:
        valor = produto.__dict__[chave]

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

    print(insercao)

    cur.execute(insercao)

    con.commit()
    con.close()
