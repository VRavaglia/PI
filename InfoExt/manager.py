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
			'hp', 'lexar', 'ocpc', 'adata', 'g_skill', 'asus', 'gainward', 'zotac',
			'sapphire', 'asrock', 'xfx', 'powercolor']#, 'Unknown']

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
			capacidade = re.search(r'[1-9]([0-9]+)?(GB|TB)', nome)
			if capacidade:
				capacidade = capacidade.group()
			frequencia = re.search(r'[1-9]([0-9]+)?(\s)?M(Hz|hz)', nome)
			if frequencia:
				frequencia = frequencia.group()
			ddr = re.search(r'DDR(-)?[1-9]([0-9]+)?(-[0-9]+)?', nome)
			if ddr:
				ddr = ddr.group()
			latencia = re.search(r'C(L)?[1-9]([0-9]+)?', nome)		#conferir
			if latencia:
				latencia = latencia.group()
			quantidade = None
			modelo = nome.split(' - ')[-1]
			info_adicionais = nome.split(',')[0]
			aux = normString(info_adicionais,marca)
			if aux:
				info_adicionais = aux
			if frequencia:
				info_adicionais = re.sub(frequencia, '', info_adicionais)
			info_adicionais = info_adicionais.split(' ')
			info_adicionais = [i for i in info_adicionais if i.lower() != marca]
			removables = [ddr, latencia, capacidade, modelo]			#mais comportados
			info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

			p_list.append(Ram('kabum.com.br',#site,
									nome,
									preco,
									desconto,
									link,
									modelo,
									marca,
									capacidade,
									frequencia,
									ddr,
									latencia,
									quantidade,
									info_adicionais))

		elif p_type == 'gpu':
			fabricante = exMarca(re.sub(r',',r' ',nome), pBrands)
			if fabricante == 'Unknown':
				if re.search(r'(^|\s)(radeon|r(x|9)(\s)?(39|55|68)00?)', nome, flags=re.IGNORECASE):#talvez refinar
					fabricante = 'amd'
				elif re.search(r'(^|\s)(geforce|(gtx?)(\s)?7[0-9]0)', nome, flags=re.IGNORECASE):#talvez refinar
					fabricante = 'nvidia'
			marca = exMarca(re.sub(r',',r' ',nome),[i for i in brands if i not in pBrands])
			vram = re.search(r'[1-9]([0-9]+)?GB', nome)
			if not vram:
				vram = re.search(r'[1-9]([0-9]+)?G', nome)
			if vram:
				vram = vram.group()

			modelo = nome.split(' - ')[-1]
			info_adicionais = nome.split(',')[0]
			aux = normString(info_adicionais,fabricante)
			if aux:
				info_adicionais = aux
			info_adicionais = info_adicionais.split(' ')
			info_adicionais = [i for i in info_adicionais if (i.lower() != marca or i.lower != fabricante)]
			removables = [vram]			#mais comportados
			info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

			p_list.append(Gpu('kabum.com.br',#site,
									nome,
									preco,
									desconto,
									link,
									modelo,
									marca,
									fabricante,
									vram,
									info_adicionais))

if __name__ == '__main__':
	from random import randint

	#catalogo = initCat(brands)
	#print(brands)
	p_type = 'gpu'#'ram'
	pecas = main_bypasser(p_type)
	pprint(pecas[:10])
	prod_list = (p_type, list())
	manageProd(pecas,prod_list)
	m_val = int(len(prod_list[1])/10)
	a = randint(1,m_val-1)
	for prod in prod_list[1][(a-1)*10:a*10]:
		#if prod.marca == 'Unknown':
		prod.parametros()
		#pprint(vars(prod))
		print('-'*50)
