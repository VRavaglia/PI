
from enum import Enum
import kabum as kb
import pichau as pch
import sys
from pprint import pprint

# [string produto,real preço cartao,real  preço boleto] = webscrape(enum site, enum tipo_peça)
def listar_todos_por_tipo(loja, tipo_peca):
	pecas = []
	if loja == 'kabum': # trocar por um case quando a tb for adicionada
		pecas = kb.listar_todos_por_tipo(tipo_peca)
	elif loja == 'pch': # trocar por um case quando a tb for adicionada
		pecas = pch.pichau_listar_todos_por_tipo(tipo_peca)
	else:
		print("Loja errada!: ", loja)
	return pecas

def main_bypasser(option):
	return listar_todos_por_tipo('pch',option)

def main():
	print(sys.argv[1])
	pecas = listar_todos_por_tipo('pch', sys.argv[1])
	pprint(pecas)
	# print(len(pecas))
	return pecas

if __name__ == "__main__":
	main()
