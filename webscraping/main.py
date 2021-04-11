
from enum import Enum
import kabum as kb
from pprint import pprint

Lojas = Enum('Loja', 'kabum terabyteshop')

# [string produto,real preço cartao,real  preço boleto] = webscrape(enum site, enum tipo_peça)
def listar_todos_por_tipo(loja, tipo_peca):
    pecas = []
    if loja == Lojas.kabum: # trocar por um case quando a tb for adicionada
        pecas = kb.listar_todos_por_tipo(tipo_peca)
    
    return pecas


def main():
    pecas = listar_todos_por_tipo(Lojas.kabum, 'mobo')
    pprint(pecas)

if __name__ == "__main__":
    main()
