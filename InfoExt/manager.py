#! /usr/bin/python3

import re
from mainWebscraping import main_bypasser
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
			'aorus', 'oex_game', 'xwise', 'maxxtro', 'hoopson', 'evus', 'tronos',
			'addlink', 'silicon_power', 'samsung', 'ktrok', 'kazuk', 'mitsushiba',
			'team_group', 'duex', 'pichau_gaming', 'super_flower', 'azza', 'mancer',
			'tgt', 'aigo', 'dt3_sports', 'pcyes'] + pBrands

mock_brands = ['lancool', 'odyssey_black', 'gamer_pichau', 'pichau_basic', 'pcyes!']

regexes = {'frequencia': r'[1-9]((\.)?[0-9]+)?\s?(M|G)?(H|h)(Z|z)(\s?\([1-9]\.?[0-9]+G(H|h)z(\s(M|m)ax)?(\s((T|t)urbo|(B|b)oost))?\))?',
				'ddr': r'DDR(-)?[1-9]([0-9]+)?(-[0-9]+)?L?', 'vram': [r'[1-9]([0-9]+)?GB', r'[1-9]([0-9]+)?G'],
				'latencia': r'CL?\s?[1-9]([0-9]+)?', 'socket': r'((FC)?LGA\s?[1-9][0-9]+|AM(3|4)\+?|s?(W|T)RX?(4|8)|SP3|FM2\+?)', #r'((LGA|B)(\s)?[1-9][0-9]+|AM4|s?TRX?4|SP3)',
				'capacidade': r'[1-9]([0-9]+)?\s?((G|g|T|t)(B|b))(\s?\([1-9]x[0-9]+GB\))?', 
				'chipset': r'[A-Z][1-9][0-9]+\s?(M|I|N)|(B|Z)(4|5)(5|6|9)0|((T|W)R)?X(57|4|8)0|((I|i)nte)?\s?X299X?|(H|h)(8|6|4)(1|7)0?',
				'tamanho': r'((E|e)(xtended)?|(m|M)(icro|ini)?|u|XL)?(\s|-)?(A|S|D|I)TX',
				'quantidade': r'[1-9](x|X)[1-9]([0-9]+)?(GB)?',
				'integrada': [r'((I|i)ntel\s)?HD\s(G|g)raphics|i(3|5|7)-[1-9]([0-9]+)?(F|f|K|k)?', r'[1-9][0-9]+G'],		#intel/amd
				'potencia': r'[1-9]([0-9]+)?W', 'modularidade': r'((S|s)emi(\s|-))?(M|m)odular',
				'selo': r'80\s?(P|p)lus(\s((B|b)ronze|(S|s)ilver|(G|g)old|((P|p)lati|(T|t)ita)num|(W|w)hite))?',
				'c_tam': r'(((M|m)i(d|ni|cro)|(F|f)ull)(-|\s)?(T|t)ower|(m|u)?ATX|ITX)',
				'dimensoes': r'[1-9]\.[0-9]((´+)|-C)?(?!\s?(G|M)Hz|MB/s)'}

def initCat(brands):
	catalog = dict()
	for brand in brands:
		catalog[brand] = list()
	return catalog

def manageProd(products,plist):
	p_type, p_list = plist
	for product in products:
		nome = re.sub(r'\s+$', '', product['nome'])
		site = product['site']
		if not re.search(r'^((K|k)it|(S|s)uporte|(C|c)abo)|(F|f)Ita|(C|c)ase\s((M|m)ultilaser\s)?p(\/|ara)\sHD|(G|g)aveta|(A|a)daptador|(F|f)(ita|onte\s(E|e)stabilizada\s(C|c)haveada)', nome):#####conf
			preco = product['preco']
			desconto = product['preco_desconto']
			link = product['link']
			marca = exMarca(re.sub(r',',r' ',nome),brands)
			if p_type == 'ram':
				if not re.search(r'(M|m)\.2', nome):
					capacidade = re.search(regexes['capacidade'], nome)
					if capacidade:
						capacidade = capacidade.group()
						quantidade = re.search(regexes['quantidade'], capacidade)
						mult = 1000 if re.search('TB',capacidade) else 1
						capacidade = int(re.search(r'[1-9]([0-9]+)?', capacidade).group())*mult
					if not quantidade:
						quantidade = re.search(regexes['quantidade'], nome)
					if quantidade:
						quantidade = re.search(r'[1-9]([0-9]+)?(x|X)', quantidade.group())
						quantidade = int(quantidade.group()[:-1])
					else:
						quantidade = 1
					frequencia = re.search(regexes['frequencia'], nome)
					if frequencia:
						frequencia = frequencia.group()
					ddr = re.search(regexes['ddr'], nome)
					if ddr:
						ddr = ddr.group()
					else:
						if int(frequencia[:-3]) > 2132:
							ddr = 'DDR4'
						else:
							ddr = 'DDR3'
					latencia = re.search(regexes['latencia'], nome)
					if latencia:
						latencia = re.sub(r'(CL?\s?)([1-9]+)','\2', latencia.group())
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

					p_list.append(Ram(site,
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

				p_list.append(Gpu(site,
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
				if not socket:
					if re.match(r'(amd|asrock|asus|gigabyte)',marca):
						if re.match(r'(A|B|X)(4|5)(2|5|7)0M?',chipset):
							socket = 'AM4'
						if marca == 'asus' and re.match(r'B460(I|M)',chipset):
							socket = 'LGA 1200'
					elif marca == 'msi':
						if re.match(r'B365M',chipset):
							socket = 'LGA 1151'
				if not socket:
					if re.search(r'1200',nome):
						socket = "LGA 1200"
					elif re.search(r'J4005I',nome):
						socket = "FCBGA1090"
				tamanho = re.search(regexes['tamanho'], nome)
				if tamanho:
					tamanho = 'mATX' if re.search(r'((M|m)(icro\s?)?|u)ATX',tamanho.group()) else re.sub('^\s','',tamanho.group())
				if not tamanho and chipset:
					if chipset[-1].lower() == 'm':
						tamanho = 'mATX'#'uATX'
					else:
						tamanho = 'ATX'
				ddr = re.search(regexes['ddr'], nome)
				if ddr:
					ddr = ddr.group()
				elif re.match(r'AM4|LGA\s?1200', str(socket)):
					ddr = "DDR4"
				if re.match(r'(asrock|msi|amd)',marca) and not ddr:
					if re.match(r'(X570|B460|H410)M', chipset):
						ddr = 'DDR4'
				modelo = re.search(r'ROG\s(Maximus\sXII|Crosshair\sVIII)\s(Extreme|Formula|Apex|Hero|Impact)|MAG\sB[1-9][0-9]+M?\s(Bazooka|Tomahawk)',nome)#gambiarra
				if modelo:
					modelo = modelo.group()
				if not modelo:
					modelo = nome.split(' - ')[-1]
					if ' ' in slicer(modelo):
						modelo = nome.split(' ')[-1]
				info_adicionais = nome.split(',')[0]
				aux = normString(info_adicionais,marca)
				if aux:
					info_adicionais = aux
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [ddr, tamanho, chipset, modelo]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Mobo(site,
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
				elif re.search(r'1[0-1][1-9]00', nome):
					socket = "FCLGA1200"
				elif re.search(r'9[1-9]00', nome):
					socket = "FCLGA1151"
				elif re.search(r'39[5-9]0(x|X)', nome):
					socket = "sTRX4"
				elif re.search(r'(3|2)(2|4)00', nome):
					socket = "AM4"
				frequencia = re.search(regexes['frequencia'], nome)
				if frequencia:
					frequencia = frequencia.group()
				###############prob????#######################
				
				integrada = False
				if marca == 'intel':
					integrada = re.search(regexes['integrada'][0], nome)
					if integrada:
						if re.search(r'[0-9](F|f|K|k)',integrada.group()):
							integrada = False
						else:
							integrada = True
				elif marca == 'amd':
					integrada = re.search(regexes['integrada'][1], nome)
				else:
					integrada = False
				if integrada:
					integrada = True #integrada.group()
				else:
					integrada = False
				############################################
				modelo = nome.split(' - ')[-1]
				if ' ' in slicer(modelo):
					modelo = nome.split(' ')[-1]
				info_adicionais = nome.split(',')[0]
				aux = normString(info_adicionais,marca)
				if aux:
					info_adicionais = aux
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [frequencia, integrada, socket, modelo]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Cpu(site,
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
				else:
					potencia = re.search(r'[1-9]([0-9]+)?', nome)
					if potencia:
						potencia = potencia.group()
					

				selo = re.search(regexes['selo'],nome)
				if selo:
					selo = selo.group()
				else:
					selo = ""
				modularidade = re.search(regexes['modularidade'],nome)
				if modularidade:
					modularidade = 0.5 if re.search(r'(S|s)emi',modularidade.group()) else 1.
				else:
					modularidade = .0

				modelo = nome.split(' - ')[-1]
				info_adicionais = nome.split(',')[0]
				info_adicionais = info_adicionais.split(' ')
				info_adicionais = [i for i in info_adicionais if i.lower() != marca]
				removables = [potencia]			#mais comportados
				info_adicionais = ' '.join([i for i in info_adicionais if i not in removables])

				p_list.append(Psu(site,
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
					elif marca == 'gamer_pichau' or marca == 'pichau_basic':
						marca = 'pichau_gaming'
					elif marca == 'pcyes!':
						marca = 'pcyes'
				tamanho = re.search(regexes['c_tam'], nome)
				if tamanho:
					tamanho = tamanho.group()
				else:
					tamanho = ""

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

				p_list.append(Case(site,
										nome,
										preco,
										desconto,
										link,
										modelo,
										marca,
										tamanho,
										info_adicionais))

			elif p_type == 'hd' or p_type == 'ssd':
				if not re.search('(E|e)xterno|(^|\s)(C|c)ase\s|(D|d)ock|(D|d|N|n)(a|A)(s|S)',nome):					
					capacidade = re.search(regexes['capacidade'],nome)
					if capacidade:
						capacidade = capacidade.group()
						mult = 1000 if re.search('TB',capacidade) else 1
						capacidade = int(re.search(r'[1-9]([0-9]+)?', capacidade).group())*mult
					dimensoes = re.search(regexes['dimensoes'],nome)
					if dimensoes:
						dimensoes = re.sub('´', '', dimensoes.group())
					else:
						dimensoes = 0	
					dimensoes = float(dimensoes)
					ssd = re.search(r'ssd',nome,flags=re.IGNORECASE)
					ssd = True if ssd else False
#					if ssd:
#						ssd = True
#					else:
#						ssd = False
#								
					sata = re.search(r'sata',nome,flags=re.IGNORECASE)
					sata = True if sata else False
#					if sata:
#						sata = True
#					else:
#						sata = False

					nvme = re.search(r'nvme',nome,flags=re.IGNORECASE)
					if nvme:
						nvme = True
						sata = False
						ssd = True
					else:
						nvme = False

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

					p_list.append(Hd(site,
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

def checker(prod_list):
	p_type, p_list = prod_list
	if p_type == 'ram':
		for product in p_list:
			if not product.ddr:
				if re.match(r'AX4U320038G16A-DR10',product.modelo):
					product.updater(ddr='DDR4')
			if not product.latencia:
				if re.match(r'AX4U3(2|6)00(38|716)G1(6|8)A-D?CBK20',product.modelo):
					product.updater(latencia='CL19')#' 19-19-19')
				elif re.search(r'Memória\sGeil\sPotenza\sEVO(\sSuper\sLuce)?',product.modelo):
					product.updater(latencia='CL16')#'-18-18-36')
				elif re.match(r'OXY16S11/4G',product.modelo):
					product.updater(latencia='CL9')
				elif re.match(r'OXY16LS11/4G',product.modelo):
					product.updater(latencia='CL11')
				else:
					product.updater(latencia='NCL')


	elif p_type == 'cpu':
		for product in p_list:
			if not product.socket:
				if product.marca == 'amd':
					if re.match(r'100-100000(167|08(6|7))WOF', product.modelo):
						product.updater(socket='sWRX8')
					if re.match(r'AD540KOKHJBOX', product.modelo):
						product.updater(socket='FM2')
				elif product.marca == 'intel':
					if re.match(r'BX80701G6400', product.modelo):
						product.updater(socket='FCLGA1200')
	elif p_type == 'mobo':
		for product in p_list:
			if not product.chipset:
				if re.match(r'ROG\sMaximus\sXII\s(Extreme|Formula|Apex|Hero)', product.modelo):
					product.updater(chipset='Z490')
				if re.match(r'ROG\sCrosshair\sVIII\sImpact', product.modelo):
					product.updater(chipset='X570')
			if not product.tamanho:
				if re.match(r'90MB1590-M0AAY0', product.modelo):
					product.updater(tamanho='Extended ATX')
			if not product.ddr:
				if re.match(r'90(MB1590-M0AAY0|-MXBDG0-A0UAYZ)|MAG.+(Bazooka|Tomahawk)', product.modelo):
					product.updater(ddr='DDR4')
				elif re.match(r'Placa-Mãe\sTUF\sGaming\sB450M-Plus', product.info_ad):
					product.updater(ddr='DDR4')
				# elif re.match(r'b450|b460|b550|a520',product.link.lower()):
				# 	product.updater(ddr='DDR4')

if __name__ == '__main__':
	from random import randint

	#catalogo = initCat(brands)
	#print(brands)
	for p_type in ['ram', 'cpu', 'mobo', 'gpu', 'case', 'psu', 'hd', 'ssd']:
		print('-'*50+'\n'+'-'*50)
		print('p_type: {}'.format(p_type))
		print('-'*50+'\n'+'-'*50)
		#input('Continue?')
		pecas = main_bypasser(p_type)
		#pprint(pecas); input()
		prod_list = (p_type, list())
		manageProd(pecas,prod_list)
		m_val = int(len(prod_list[1])/10)
		#a = randint(1,m_val-1)
		#for prod in prod_list[1][(a-1)*10:a*10]:
		checker(prod_list)
		#print('There are {} products'.format(len(prod_list[1])))
		for prod in prod_list[1]:
			if prod.marca == 'Unknown':
				prod.parametros()
				print('-'*50)
