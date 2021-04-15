
from enum import Enum
import kabum as kb
import sys
from pprint import pprint

Lojas = Enum('Loja', 'kabum terabyteshop')

# [string produto,real preço cartao,real  preço boleto] = webscrape(enum site, enum tipo_peça)
def listar_todos_por_tipo(loja, tipo_peca):
	pecas = []
	if loja == Lojas.kabum: # trocar por um case quando a tb for adicionada
		pecas = kb.listar_todos_por_tipo(tipo_peca)
	return pecas

def main_bypasser(option):
	return listar_todos_por_tipo(Lojas.kabum,option)

def main():
	print(sys.argv[1])
	pecas = listar_todos_por_tipo(Lojas.kabum, sys.argv[1])
	pprint(pecas)
	#return pecas

if __name__ == "__main__":
	main()
