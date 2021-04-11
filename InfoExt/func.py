#! /usr/bin/python3

import re

def slicer(string):
	return [char for char in string]

def popFst(lst):
	lst.reverse()
	lst.pop()
	lst.reverse()
	return lst

def normString(string, brand):
	if '_' not in slicer(brand):
		return None
	split_brand = brand.split('_')
	regex_str = r'[.|\s|-]'.join(split_brand)
	if not re.search(regex_str, string.lower()):
		return None
	return re.sub(regex_str, brand, string, flags=re.IGNORECASE)

def exMarcas(strs, catalog):
	for s in strs:
		found = False
		for key in catalog.keys():
			if '_' in slicer(key):
				n_string = normString(s,key)
				if n_string:
					aux = [i for i in n_string.split() if i.lower() != key]
					catalog[key].append(' '.join(aux))
					found = True
					break
			elif key in s.lower().split():
				aux = [i for i in s.split() if i.lower() != key]
				catalog[key].append(' '.join(aux))
				found = True
				break
		if not found:
			catalog['Unknown'].append(s)

def rPrioridade(catalog, pBrands=['dell','lenovo']):
	for key in catalog.keys() - pBrands:
		cur_cat = catalog[key].copy()
		for prod in cur_cat:
			for brand in pBrands:
				if brand in prod.lower().split():
					aux = [i for i in prod.split() if i.lower() != brand] + ['(OBS.: c/ {})'.format(key)]
					catalog[brand].append(' '.join(aux))
					catalog[key].remove(prod)
					break
	for i,brand in enumerate(pBrands):		#checa prioridade entre as marcas prioritárias
		for key in pBrands[i:]:
			if key not in catalog.keys():
				break
			cur_cat = catalog[key].copy()
			for prod in cur_cat:
				if brand in prod.lower().split():
					aux = [i for i in prod.split() if i.lower() != brand] + ['(OBS.: c/ {})'.format(key)]
					catalog[brand].append(' '.join(aux))
					catalog[key].remove(prod)
					break

if __name__ == '__main__':
	catalogo = {
		'lenovo': list(),
		'intel': list(),
		'amd': list(),
		'kingston': list(),
		'nvidia': list(),
		'dell': list(),
		'sharkoon': list(),
		'corsair': list(),
		'cooler_master': list(),
		'Unknown': list()
	}
	m_prioridades = ['amd', 'nvidia']
	strings = [
		'Bacalhau da Cananeia',
		'Placa de video asus nvidia geforce gtx 1050',
		'plca de video PowerColor AMD radeon rx 550',
		'placa de video PowerColor ardeon rx amd 550',
		'Bolo de Fubá da Intel_gencia',
		'placa de video powercolor amd radeon rx 552',
		'Notebook Dell Inspiron 3583-AS80P Intel Core i5 - 8GB 256GB SSD 15,6” Placa Vídeo 2GB Windows 10',
		'Omelete de Amdiar',
		'pl_ca de Vídeo PowerColor intEl radeon rx 772',
		'Gabinete Sharkoon TG5 Red Vidro Temperado 4mm Led Fan 12cm ATX',
		'Cooler Processador Hyper H412R RR-H412-20PK-R2 Cooler Master',
		'Cooler processador Hyper H412R_RR-H412-20PK-R2 Cooler-Master',
		'Cooler processador Hyper XXXX_XXR-H412-20PK-R2 Cooler.Master',
		'Memória Corsair Vengeance LP 4GB (2x2GB) 1600Mhz DDR3 C9 Black - CML4GX3M2A1600C9',
		'PC gamer lenovo pisca led intel i7 dell',
		'intel core i5, Notebook Dell Inspiron 3583-AS80P - 8GB 256GB SSD 15,6” Placa Vídeo 2GB Windows 10',
		'Gabinete Sharkoonado TG5 Red Vidro Temperado 4mm Led Fan 12cm ATX'
	]
	exMarcas(strings,catalogo)
	rPrioridade(catalogo)#, pMarcas=m_prioridades)
	for key in catalogo.keys():
		print('-'*40)
		print('Marca: {}'.format(key))
		print('-'*40)
		print('Produtos:')
		for i in catalogo[key]:
			print('\t{}'.format(i))
