const express = require('express');
const router = express.Router();
const dbService = require('../services/db-service')
router.use(express.json())

// Checagem de compatibilidade
var filtrosGlobais = {
    socket : '',
    tamanho : '',
    ddr : ''
}

// Lista de produtos escolhidos
var listaProdutos = {
}

// Request POST pra procurar na DB,
// o body precisa conter os campos: "tipo", "filtros" (com todos os filtros, utilizando eles ou nao)
router.post('/', async (req, res) => {
    const listOfProds = await dbService.listProd(req.body.tipo, req.body.filtros, filtrosGlobais);
    res.status(200).send(listOfProds);
})

// Request GET pra pegar a lista de produtos escolhidos
router.get('/', async (req, res) => {
    res.status(200).send(listaProdutos)
})

// DEBUG: Request GET pra pegar a lista de filtros globais
router.get('/filtros', async (req, res)=>{
    res.status(200).send(filtrosGlobais)
})

// Request POST pra adicionar um produto na lista.
// o body precisa conter os campos: "tipo" e "link" (com o link do produto)
router.post('/add', async (req, res) => {
    const produtoEscolhido = await dbService.listProd(req.body.tipo, {
        "marca":"",
        "socket":"",
        "tamanho":"",
        "ddr": "",
        "capacidade":"",
        "vram":"",
        "integrada":"",
        "fabricante":"",
        "ssd":"",
        "frequencia":"",
        "selo":"",
        "nvme":"",
        "sata":"",
        "link":req.body.link
      }, filtrosGlobais)
    if (typeof listaProdutos[req.body.tipo] == 'undefined'){
        listaProdutos[req.body.tipo] = produtoEscolhido[0]
        if (req.body.tipo == "mobo"){
            filtrosGlobais["socket"] = produtoEscolhido[0].socket
            filtrosGlobais["tamanho"] = produtoEscolhido[0].tamanho
            filtrosGlobais["ddr"]  = produtoEscolhido[0].ddr
        }
        else if (req.body.tipo == "cpu"){
            filtrosGlobais["socket"] = produtoEscolhido[0].socket
        }
        else if (req.body.tipo == "ram"){
            filtrosGlobais["ddr"] = produtoEscolhido[0].ddr
        }

        res.status(200).send({"adicionado": true})
    }
    else {
        res.status(200).send({"adicionado": false})
    }
})

// Request POST pra remover um produto da lista
// o body precisa conter os campos: "tipo" e "link" (com o link do produto)
router.post('/remove', async (req, res) => {
    if (typeof listaProdutos.mobo !== 'undefined'){
        if (listaProdutos.mobo.link == req.body.link){
            delete listaProdutos.mobo;
            filtrosGlobais.tamanho = ''
            if (typeof listaProdutos.cpu == 'undefined'){
                filtrosGlobais.socket = ''
            }
            if (typeof listaProdutos.ram == 'undefined'){
                filtrosGlobais.ddr = ''
            }
        }
    }
    if (typeof listaProdutos.cpu !== 'undefined'){
        if (listaProdutos.cpu.link == req.body.link){
            delete listaProdutos.cpu;
            if (typeof listaProdutos.mobo == 'undefined'){
                filtrosGlobais.socket = ''
            }
        }
    }
    if (typeof listaProdutos.gpu !== 'undefined'){
        if (listaProdutos.gpu.link == req.body.link){
            delete listaProdutos.gpu;
        }
    }
    if (typeof listaProdutos.case !== 'undefined'){
        if (listaProdutos.case.link == req.body.link){
            delete listaProdutos.case;
        }
    }
    if (typeof listaProdutos.ram !== 'undefined'){
        if (listaProdutos.ram.link == req.body.link){
            delete listaProdutos.ram;
            if (typeof listaProdutos.mobo == 'undefined'){
                filtrosGlobais.ddr = ''
            }
        }

    }
    if (typeof listaProdutos.psu !== 'undefined'){
        if (listaProdutos.psu.link == req.body.link){
            delete listaProdutos.psu;
        }
    }
    if (typeof listaProdutos.hd !== 'undefined'){
        if (listaProdutos.hd.link == req.body.link){
            delete listaProdutos.hd;
        }
    }
    res.status(200).send()
})


// router.get('/profit', async (req, res) => {
//     const profit = await dbService.calculateProfit();
//     res.status(200).send(profit);
// })

module.exports = router;