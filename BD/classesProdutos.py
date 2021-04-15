class Produto:
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, info_adicionais):
		self.site = site
		self.nome = nome
		self.preco = preco
		self.preco_desconto = preco_desconto
		self.link = link
		self.modelo = modelo
		self.marca = marca
		self.info_ad = info_adicionais

	def parametros(self):
		print('Site: {}'.format(self.site))
		print('Nome: {}'.format(self.nome))
		print('Preco: R${}'.format(self.preco))
		print('Desconto: R${}'.format(self.preco_desconto))
		print('Link: {}'.format(self.site + self.link))
		print('Modelo: {}'.format(self.modelo))
		print('Marca: {}'.format(self.marca))

	def info_adicionais(self):
		print('Info Adicionais: {}'.format(self.info_ad))

class Mobo(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, chipset, socket, tamanho, ddr, info_adicionais):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca, info_adicionais)
		self.chipset = chipset
		self.socket = socket
		self.tamanho = tamanho
		self.ddr = ddr
		self.tipo = 'Mobo'

	def parametros(self):
		super().parametros()
		print('Chipset: {}'.format(self.chipset))
		print('Socket: {}'.format(self.socket))
		print('DDR: {}'.format(self.ddr))
		print('Tamanho: {}'.format(self.tamanho))
		if self.info_ad:
			self.info_adicionais()

	def info_adicionais(self):
		super().info_adicionais()
class Psu(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, selo, potencia, modularidade):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
		self.selo = selo
		self.potencia = potencia
		self.modulariade = modulariade
		self.tipo = 'Psu'

class Cpu(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, socket, frequencia, integrada):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
		self.socket = socket
		self.frequencia = frequencia
		self.integrada = integrada
		self.tipo = 'Cpu'

class Ram(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, capacidade, frequencia, ddr, latencia, quantidade,info_adicionais):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca,info_adicionais)
		self.capacidade = capacidade
		self.frequencia = frequencia
		self.ddr = ddr
		self.latencia = latencia
		self.quantidade = quantidade
		self.tipo = 'Ram'

	def parametros(self):
		super().parametros()
		print('Capacidade: {}'.format(self.capacidade))
		print('Frequência: {}'.format(self.frequencia))
		print('DDR: {}'.format(self.ddr))
		print('Latencia: {}'.format(self.latencia))
		print('Quantidade: {}'.format(self.quantidade))
		if self.info_ad:
			self.info_adicionais()

	def info_adicionais(self):
		super().info_adicionais()

class Hd(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, dimensoes, ssd, nvme, sata):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
		self.dimensoes = dimensoes
		self.ssd = ssd
		self.nvme = nvme
		self.sata = sata
		self.tipo = 'Hd'


class Gpu(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, fabricante, vram, info_adicionais):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca,info_adicionais)
		self.fabricante = fabricante
		self.vram = vram
		self.tipo = 'Gpu'

	def parametros(self):
		super().parametros()
		print('Fabricante: {}'.format(self.fabricante))
		print('VRam: {}'.format(self.vram))
		if self.info_ad:
			self.info_adicionais()

	def info_adicionais(self):
		super().info_adicionais()


class Case(Produto):
	def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, fabricante, tamanho):
		super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
		self.tamanho = fabricante
		self.tipo = 'Case'
