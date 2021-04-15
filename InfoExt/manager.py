#! /usr/bin/python3

import re
from main import main_bypasser
from classesProdutos import *
from func import exMarca, normString
from pprint import pprint

pBrands = ['nvidia', 'amd']
brands = pBrands + ['cooler_master', 'evga', 'corsair', 'thermaltake', 'pcyes', 'gigabyte',
			'aerocool', 'redragon', 'patriot', 'hyperx', 'crucial', 'msi', 'galax', 'pny',
			'deepcool', 'afox','colorful', 'biostar', 'seagate', 'sandisk', 'kingston',
			'western_digital', 'toshiba', 'hikvision', 'nzxt', 'lian_li', 'xpg', 'husky',
			'hp', 'lexar', 'ocpc', 'adata', 'g_skill']#, 'Unknown']

def initCat(brands):
	catalog = dict()
	for brand in brands:
		catalog[brand] = list()
	return catalog

def manageProd(products,plist):
	p_type, p_list = plist
	for product in products:
		nome = product['nome']
		preco = product['preco']
		desconto = product['preco_desconto']
		link = product['link']
		marca = exMarca(re.sub(r',',r' ',nome),brands)
		if p_type == 'ram':
			capacidade = None
			frequencia = re.search(r'[1-9]([0-9]+)?(\s)?M(Hz|hz)', nome)
			if frequencia:
				frequencia = frequencia.group()
			tamanho = re.search(r'[1-9]([0-9]+)?(GB|TB)', nome)
			if tamanho:
				tamanho = tamanho.group()
			ddr = re.search(r'DDR(-)?[1-9]([0-9]+)?(-[0-9]+)?', nome)
			if ddr:
				ddr = ddr.group()
			latencia = re.search(r'C(L)?[1-9]([0-9]+)?', nome)		#conferir
			if latencia:
				latencia = latencia.group()
			quantidade = None
			modelo = nome.split(',')[0]
			aux = normString(modelo,marca)
			if aux:
				modelo = aux
			if frequencia:
				modelo = re.sub(frequencia, '', modelo)
			modelo = modelo.split(' ')
			modelo = [i for i in modelo if i.lower() != marca]
			removables = [ddr, latencia, tamanho]			#mais comportados
			modelo = ' '.join([i for i in modelo if i not in removables])

			p_list.append(Ram(nome,
									preco,
									desconto,
									link,
									modelo,
									marca,
									capacidade,
									frequencia,
									tamanho,
									ddr,
									latencia,
									quantidade))

if __name__ == '__main__':
	#catalogo = initCat(brands)
	print(brands)
	p_type = 'ram'
	pecas = main_bypasser(p_type)
	ram_list = (p_type, list())
	manageProd(pecas,ram_list)
	for prod in ram_list[1][:10]:
		#if prod.marca == 'Unknown':
		prod.parametros()
		#pprint(vars(prod))
		print('-'*50)
