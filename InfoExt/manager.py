#! /usr/bin/python3

import re
from main import main_bypasser
from classesProdutos import *
from func import exMarca, normString, slicer
from pprint import pprint

pBrands = ['nvidia', 'amd']
brands = ['cooler_master', 'evga', 'corsair', 'thermaltake', 'pcyes', 'gigabyte',
			'aerocool', 'redragon', 'patriot', 'hyperx', 'crucial', 'msi', 'galax', 'pny',
			'deepcool', 'afox','colorful', 'biostar', 'seagate', 'sandisk', 'kingston',
			'western_digital', 'toshiba', 'hikvision', 'nzxt', 'lian_li', 'xpg', 'husky',
			'hp', 'lexar', 'ocpc', 'adata', 'g_skill', 'asus', 'gainward', 'zotac',
			'sapphire', 'asrock', 'xfx', 'powercolor', 'intel', 'one_power', 'gamemax',
			'c3_tech', 'brazil_pc', 'seasonic', 'cougar', 'bluecase', 'apex_gaming',
			'sharkoon', 'powerx', 'nox', 't-dagger', 'fortrek', 'c3_plus', 'warrior',
			'vinik', 'pixxo', 'k_mex', 'rise_mode', 'lacie', 'asustor', 'qnap', 'wd',
			'synology', 'f3', 'oxy', 'geil', 'tarct', 'bitfenix', 'gamdias', 'nzxt',
			'aorus', 'oex_game', 'xwise', 'maxxtro', 'hoopson', 'evus', 'tronos'] + pBrands

mock_brands = ['lancool', 'odyssey_black']

regexes = {'frequencia': r'[1-9]((\.)?[0-9]+)?\s?(M|G)(H|h)z(\s?\([1-9]\.?[0-9]+G(H|h)z(\s(M|m)ax)?(\s((T|t)urbo|(B|b)oost))?\))?',
				'ddr': r'DDR(-)?[1-9]([0-9]+)?(-[0-9]+)?', 'vram': [r'[1-9]([0-9]+)?GB', r'[1-9]([0-9]+)?G'],
				'latencia': r'C(L)?[1-9]([0-9]+)?', 'socket': r'((FC)?LGA\s?[1-9][0-9]+|AM(3|4)\+?|s?(W|T)RX?(4|8)|SP3|FM2\+?)', #r'((LGA|B)(\s)?[1-9][0-9]+|AM4|s?TRX?4|SP3)',
				'capacidade': r'[1-9]([0-9]+)?(GB|TB)', 'chipset': r'(([A-Z])[1-9][0-9]+M|(B|Z)(4|5)(5|6|9)0|X570)',
				'tamanho': r'((E|e)xtended|(m|M)(icro|ini)?|u)?(\s|-)?(A|S|D|I)TX',
				'quantidade': r'[1-9](x|X)[1-9]([0-9]+)?(GB)?',
				'integrada': [r'((I|i)ntel\s)?HD\s(G|g)raphics', r'[1-9][0-9]+G'],		#intel/amd
				'potencia': r'[1-9]([0-9]+)?W', 'modularidade': r'((S|s)emi(\s|-))?(M|m)odular',
				'selo': r'80\s?(P|p)lus(\s((B|b)ronze|(S|s)ilver|(G|g)old|((P|p)lati|(T|t)ita)num|(W|w)hite))?',
				'c_tam': r'(((M|m)i(d|ni|cro)|(F|f)ull)(-|\s)?(T|t)ower|(m|u)?ATX|ITX)',
				'dimensoes': r'[1-9]\.[0-9]((´+)|-C)?(?!\s?(G|M)Hz)'}

def initCat(brands):
	catalog = dict()
	for brand in brands:
		catalog[brand] = list()
	return catalog

def manageProd(products,plist):
	p_type, p_list = plist
	for product in products:
		nome = re.sub(r'\s+$', '', product['nome'])
		if not re.search(r'^((K|k)it|(S|s)uporte|(C|c)abo)|(F|f)Ita|(C|c)ase\s((M|m)ultilaser\s)?p(\/|ara)\sHD|(G|g)aveta|(A|a)daptador|(F|f)(ita|onte\s(E|e)stabilizada\s(C|c)haveada)', nome):#####conf
			preco = product['preco']
			desconto = product['preco_desconto']
			link = product['link']
			marca = exMarca(re.sub(r',',r' ',nome),brands)
			if p_type == 'ram':
				capacidade = re.search(regexes['capacidade'], nome)
				if capacidade:
					capacidade = capacidade.group()
				frequencia = re.search(regexes['frequencia'], nome)
				if frequencia:
					frequencia = frequencia.group()
				ddr = re.search(regexes['ddr'], nome)
				if ddr:
					ddr = ddr.group()
				latencia = re.search(regexes['latencia'], nome)
				if latencia:
					latencia = latencia.group()
				quantidade = re.search(regexes['quantidade'], nome)
				if quantidade:
					quantidade = quantidade.group()
				else:
					quantidade = 1
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
				if marca == 'Unknown':
					marca = fabricante
				vram = re.search(regexes['vram'][0], nome)
				if not vram:
					vram = re.search(regexes['vram'][1], nome)
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

			elif p_type == 'mobo':
				socket = re.search(regexes['socket'], nome)
				if socket:
					socket = socket.group()
				chipset = re.search(regexes['chipset'], nome)
				if chipset:
					chipset = chipset.group()
				if re.match(r'(amd|asrock|asus|gigabyte)',marca) and not socket:
					if re.match(r'(A|B|X)(4|5)(2|5|7)0M?',chipset):
						socket = 'AM4'
				elif marca == 'msi':
					if re.match(r'B365M',chipset):
						socket = 'LGA 1151'
				tamanho = re.search(regexes['tamanho'], nome)
				if tamanho:
					tamanho = tamanho.group()
				if not tamanho and chipset:
					if chipset[-1].lower() == 'm':
						tamanho = 'uATX'
				ddr = re.search(regexes['ddr'], nome)
				if ddr:
					ddr = ddr.group()
				if re.match(r'(asrock|msi|amd)',marca) and not ddr:
					if re.match(r'(X570|B460|H410)M', chipset):
						ddr = 'DDR4'
				modelo = nome.split(' - ')[-1]
				info_adicionais = nome.split(',')[0]
				aux = normString(info_adicionais,marca)
				if aux:
					info_adicionais = aux
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [ddr, tamanho, chipset, modelo]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Mobo('kabum.com.br',#site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										chipset,
										socket,
										tamanho,
										ddr,
										info_adicionais))

			elif p_type == 'cpu':
				socket = re.search(regexes['socket'], nome)
				if socket:
					socket = socket.group()
				frequencia = re.search(regexes['frequencia'], nome)
				if frequencia:
					frequencia = frequencia.group()
				###############prob????#######################
				if marca == 'intel':
					integrada = re.search(regexes['integrada'][0], nome)
				elif marca == 'amd':
					integrada = re.search(regexes['integrada'][1], nome)
				else:
					integrada = None
				if  integrada:
					integrada = integrada.group()
				############################################
				modelo = nome.split(' - ')[-1]
				if ' ' in slicer(modelo):
					modelo = nome.split(' ')[-1]
				if not socket:
					if marca == 'amd':
						if re.match(r'100-100000(167|08(6|7))WOF', modelo):
							socket = 'sWRX8'
						if re.match(r'AD540KOKHJBOX',modelo):
							socket = 'FM2'
					elif marca == 'intel':
						if re.match(r'BX80701G6400',modelo):
							socket = 'FCLGA1200'
				info_adicionais = nome.split(',')[0]
				aux = normString(info_adicionais,marca)
				if aux:
					info_adicionais = aux
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [frequencia, integrada, socket, modelo]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Cpu('kabum.com.br',#site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										socket,
										frequencia,
										integrada,
										info_adicionais))

			elif p_type == 'psu':
				potencia = re.search(regexes['potencia'],nome)
				if potencia:
					potencia = potencia.group()
				selo = re.search(regexes['selo'],nome)
				if selo:
					selo = selo.group()
				modularidade = re.search(regexes['modularidade'],nome)
				if modularidade:
					modularidade = modularidade.group()

				modelo = nome.split(' - ')[-1]
				info_adicionais = nome.split(',')[0]
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [potencia]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Psu('kabum.com.br',#site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										selo,
										potencia,
										modularidade,
										info_adicionais))

			elif p_type == 'case':
				#marca = exMarca(re.sub(r',',r' ',nome),[i for i in brands if i not in pBrands])
				if marca == 'Unknown':
					marca = exMarca(re.sub(r',',r' ',nome),mock_brands)
					if marca == 'lancool':
						marca = 'lian_li'
					elif marca == 'odyssey_black':
						marca = 'k_mex'
				tamanho = re.search(regexes['c_tam'], nome)
				if tamanho:
					tamanho = tamanho.group()

				modelo = re.search(r'(BG-[0-9]+|GA[0-9]+|SGC[1-9]\s?Window)',nome)
				if modelo:
					modelo = modelo.group()
				else:
					modelo = nome.split(' - ')[-1]
					if not re.search(r'lancool',modelo,flags=re.IGNORECASE) and  ' ' in slicer(modelo):
						modelo = modelo.split(' ')[-1]
				if not tamanho:			#mock look-up table
					if re.match(r'(NXLITE0(2|3)0B?|BG-[0-9]+|32296|SGC1\s?Window|CG.+B0X|NXHUMMERTGF|RM-(CA|WT)-0(6|7)-(FB|RGB)|LANCOOL\s205\sBLACK)',modelo):
						tamanho = 'ATX'
					elif re.match(r'GA178|CC-9011116-WW|GX700',modelo):
						tamanho = 'uATX'
					elif re.match(r'CC-9011131-WW|NX(INFINTY(ALPHA|ATOM|OMEGA)|HUMMERTGM)',modelo):
						tamanho = 'Mid Tower'
				if marca == 'Unknown':
					if re.match(r'CG(01C1RH001CB0X|-0[1-9]B1)',modelo):
						marca = 'k_mex'
					elif re.match(r'Ca-H710(i|b)-(Br|W1)',modelo):
						marca = 'nzxt'
				info_adicionais = nome.split(',')[0]
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [tamanho]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Case('kabum.com.br',#site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										tamanho,
										info_adicionais))

			elif p_type == 'hd':
				capacidade = re.search(regexes['capacidade'],nome)
				if capacidade:
					capacidade = capacidade.group()
				dimensoes = re.search(regexes['dimensoes'],nome)
				if dimensoes:
					dimensoes = dimensoes.group()
				ssd = re.search(r'ssd',nome,flags=re.IGNORECASE)
				if ssd:
					ssd = ssd.group()
				nvme = re.search(r'nvme',nome,flags=re.IGNORECASE)
				if nvme:
					nvme = nvme.group()
				sata = re.search(r'sata',nome,flags=re.IGNORECASE)
				if sata:
					sata = sata.group()

				#modelo = re.search(r'(BG-[0-9]+|GA[0-9]+|SGC[1-9]\s?Window)',nome)
				modelo = None
				if modelo:
					modelo = modelo.group()
				else:
					modelo = nome.split(' - ')[-1]
					if not re.search(r'lancool',modelo,flags=re.IGNORECASE) and  ' ' in slicer(modelo):
						modelo = modelo.split(' ')[-1]
				info_adicionais = nome.split(',')[0]
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [capacidade,ssd,nvme,sata]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Hd('kabum.com.br',#site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										capacidade,
										dimensoes,
										ssd,
										nvme,
										sata,
										info_adicionais))

if __name__ == '__main__':
	from random import randint

	#catalogo = initCat(brands)
	#print(brands)
	for p_type in ['ram', 'cpu', 'mobo', 'gpu', 'case', 'psu', 'hd']:
		print('-'*50+'\n'+'-'*50)
		print('p_type: {}'.format(p_type))
		print('-'*50+'\n'+'-'*50)
		input('Continue?')
		pecas = main_bypasser(p_type)
		#pprint(pecas); input()
		prod_list = (p_type, list())
		manageProd(pecas,prod_list)
		m_val = int(len(prod_list[1])/10)
		a = randint(1,m_val-1)
		#for prod in prod_list[1][(a-1)*10:a*10]:
		for prod in prod_list[1]:
			if prod.marca == 'Unknown':
				prod.parametros()
				print('-'*50)
