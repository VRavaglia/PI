#! /usr/bin/python3

pBrands = ['nvidia', 'amd']
brands = pBrands + ['cooler_master', 'evga', 'corsair', 'thermaltake', 'pcyes', 'gigabyte',
			'aerocool', 'redragon', 'patriot', 'hyperx', 'crucial', 'msi', 'galax', 'pny',
			'deepcool', 'afox','colorful', 'biostar', 'seagate', 'sandisk', 'kingston',
			'western_digital', 'toshiba', 'hikvision', 'nzxt', 'lian_li']

def initCat(brands):
	catalog = dict()
	for brand in brands:
		catalog[brand] = list()
	return catalog

if __name__ == '__main__':
	catalogo = initCat(brands)
	print(catalogo)
