from classesProdutos import *
import sqlite3
from datetime import datetime

database = 'main.sqlite'

def class2str(atributos):
    valores = ''

    for valor in atributos:
        if type(valor) is int or type(valor) is float:
            valores = valores + ', ' + str(valor)
        else:
            valores = valores + ', \'' + valor + '\''
    valores = valores[2:]
    return valores


def inserirMobo(mobo):
    con = sqlite3.connect(database)
    cur = con.cursor()

    valores = class2str( [mobo.site, \
                        mobo.nome, \
                        mobo.preco, \
                        mobo.preco_desconto, \
                        mobo.link, \
                        mobo.modelo, \
                        mobo.marca, \
                        mobo.chipset, \
                        mobo.socket, \
                        mobo.tamanho, \
                        mobo.ddr])

    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    valores = '(' + valores + ', \'' + data + '\'' +')'

    cur.execute("INSERT INTO Mobo VALUES " + valores)

    con.commit()
    con.close()