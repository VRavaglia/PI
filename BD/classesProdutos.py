class Produto:
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca):
        self.site = site
        self.nome = nome
        self.preco = preco
        self.preco_desconto = preco_desconto
        self.link = link
        self.modelo = modelo
        self.marca = marca

class Mobo(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, chipset, socket, tamanho, ddr):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.chipset = chipset
        self.socket = socket
        self.tamanho = tamanho
        self.ddr = ddr

class Psu(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, selo, potencia, modularidade):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.selo = selo
        self.potencia = potencia
        self.modulariade = modulariade

class Cpu(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, socket, frequencia, integrada):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.socket = socket
        self.frequencia = frequencia
        self.integrada = integrada

class Ram(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, capacidade, frequencia, ddr, latencia, quantidade):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.capacidade = capacidade
        self.frequencia = frequencia
        self.ddr = ddr
        self.latencia = latencia
        self.quantidade = quantidade

class Hd(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, dimensoes, ssd, nvme, sata):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.dimensoes = dimensoes
        self.ssd = ssd
        self.nvme = nvme
        self.sata = sata

class Gpu(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, fabricante, vram):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.fabricante = fabricante
        self.vram = vram

class Case(Produto):
    def __init__(self, site, nome, preco, preco_desconto, link, modelo, marca, fabricante, tamanho):
        super().__init__(site, nome, preco, preco_desconto, link, modelo, marca)
        self.tamanho = fabricant