from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json

pichau_base = 'https://www.pichau.com.br/'
pichau_end = '&product_list_limit=48'
pichau_pg = 'p='
pichau_mobo = pichau_base + 'hardware/placa-m-e?'
pichau_psu = pichau_base + 'hardware/fonte?'
pichau_ram = pichau_base + 'hardware/memorias?'
pichau_cpu = pichau_base + 'hardware/processadores?'
pichau_gpu = pichau_base + 'hardware/placa-de-video?'
pichau_case = pichau_base + 'hardware/gabinete?'
pichau_cooler_cpu = pichau_base + 'hardware/cooler-processador?'
pichau_cooler_geral = pichau_base + 'hardware/ventoinhas-e-casemod?'
pichau_hd = pichau_base + 'hardware/hard-disk-e-ssd?'
pichau_ssd = pichau_base + 'hardware/ssd?'

DEBUG = True

def pichau_listar_todos_por_tipo(tipo):
    url_produto = {'mobo' : pichau_mobo, 'psu' : pichau_psu, 'ram' : pichau_ram, 'cpu' : pichau_cpu, 'gpu' : pichau_gpu, 'case' : pichau_case, 'cooler_cpu': pichau_cooler_cpu, 'cooler_geral': pichau_cooler_geral, 'hd': pichau_hd, 'ssd': pichau_ssd}
    
    if tipo == 'cooler':
        cooler = True
        tipo1 = 'cooler_cpu'
    else:
        cooler = False
        tipo1 = tipo
        
    continuar = True
    pagina = 1
    auxDados = []
    
    while continuar:
        arquivo_debug = '../webscraping/' + 'pch_' + tipo1 + '_' + str(pagina)+ '_debug.html'
        
        if not DEBUG:
            url = url_produto[tipo1] + pichau_pg + str(pagina) + pichau_end
            r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(r).read()    
            soup = BeautifulSoup(html, 'html.parser')
        
            f = open(arquivo_debug, 'w', encoding='latin-1')#"utf8")
            f.write(soup.prettify())
            f.close()
            
        else:
            f = open(arquivo_debug, 'r', encoding='latin-1')#"utf8")
            html = f.read()
            f.close()
            soup = BeautifulSoup(html, 'html.parser')
        
        auxDadosPagina = []
        quantidade_pg = 0
        indisponiveis = 0
        
        for dados in soup.find_all('i', 'fa fa-times'):
            indisponiveis += 1

        for dados in soup.find_all('a', 'product-item-link'):
            link = dados.get('href')
            nome = dados.string.strip()
            dictDados = {'nome' : nome, 'link' : link, 'site': 'pichau.com.br'}
            auxDadosPagina.append(dictDados)
            quantidade_pg += 1
        
        if indisponiveis != 0:
            continuar = False
            auxDadosPagina = auxDadosPagina[:48-indisponiveis]

        index = 0
        for precos in soup.find_all(attrs={"data-price-type":'finalPrice'}):
            precoBase = precos.get('data-price-amount')
            auxDadosPagina[index]['preco'] = precoBase
            index += 1
            
        for item in auxDadosPagina:
            item['preco_desconto'] = str(round(float(item['preco'])*0.88, 2))
            item['img'] = '' # Adicionar funcionalidade depois
        
        for item in auxDadosPagina:
            auxDados.append(item)
            
        if quantidade_pg != 48:
            continuar = False
            
        if continuar == False:
            if cooler == True:
                auxDados2 = pichau_listar_todos_por_tipo('cooler_geral')
                for item in auxDados2:
                    auxDados.append(item)
                stringJson = json.dumps(auxDados)
                f = open('../webscraping/' + 'pch_cooler.txt', 'w')
                f.write(stringJson)
                f.close()
            elif tipo != 'cooler_geral':
                stringJson = json.dumps(auxDados)
                f = open('../webscraping/' + 'pch_' + tipo1 + '.txt', 'w')
                f.write(stringJson)
                f.close()
        else:
            pagina += 1
            
    return auxDados

