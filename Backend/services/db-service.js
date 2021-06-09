
require('dotenv').config();
const fetch = require('node-fetch');
const dateformat = require('dateformat');
const Knex = require('knex');

const DBoptions = {
    client: 'sqlite3',
    connection: {
        filename: "./../BD/main.sqlite"
    },
    useNullAsDefault: true
}



const knex = require('knex')(DBoptions);

async function listProd(tipo, filtros, filtrosGlobais) {
    console.log("Tipo: ", tipo)
    console.log("Filtro: ", filtros)
    //filtrosJSON = JSON.parse(filtros)
    filtrosJSON = filtros

    if (tipo == "mobo"){
        if (filtrosGlobais.socket != ''){
            filtrosJSON["socket"] = filtrosGlobais.socket
        }
        if (filtrosGlobais.tamanho != ''){
            filtrosJSON["tamanho"] = filtrosGlobais.tamanho
        }
        if (filtrosGlobais.ddr != ''){
            filtrosJSON["ddr"] = filtrosGlobais.ddr
        }
    }

    if (tipo == "cpu"){
        if (filtrosGlobais.socket != ''){
            filtrosJSON["socket"] = filtrosGlobais.socket
        }
    }

    if (tipo == "ram"){
        if (filtrosGlobais.ddr != ''){
            filtrosJSON["ddr"] = filtrosGlobais.ddr
        }
    }

    console.log("JSON: ", filtrosJSON)

    var max_preco = min_preco = 0;

    console.log("Filtros utilizados:")

    const rows = await knex.from(tipo).select("*").where(
        function(){
           /* if (filtrosJSON.max_preco > 0){
                this.whereBetween('preco_desconto', [min_preco, max_preco])
                console.log("preco")
            }*/
            if (filtrosJSON.marca !== '') {
                this.where('marca', filtrosJSON.marca)
                console.log("marca")
            }
            if (filtrosJSON.socket !== ''){
                this.where('socket', filtrosJSON.socket)
                console.log("socket")
            }
            if (filtrosJSON.tamanho !== ''){
                this.where('tamanho', filtrosJSON.tamanho)
                console.log("tamanho")
            }
            if (filtrosJSON.ddr !== ''){
                this.where('ddr', filtrosJSON.ddr)
                console.log("ddr")
            }
            if (filtrosJSON.capacidade !== ''){
                this.where('capacidade', filtrosJSON.capacidade)
                console.log("capacidade")
            }
            if (filtrosJSON.vram !== ''){
                this.where('vram', filtrosJSON.vram)
                console.log("vram")
            }
            if (filtrosJSON.integrada !== ''){
                this.where('integrada', filtrosJSON.integrada)
                console.log("integrada")
            }
            if (filtrosJSON.fabricante !== ''){
                this.where('fabricante', filtrosJSON.fabricante)
                console.log("fabricante")
            }
            if (filtrosJSON.ssd !== ''){
                this.where('ssd', filtrosJSON.ssd)
                console.log("ssd")
            }
            if (filtrosJSON.nvme !== ''){
                this.where('nvme', filtrosJSON.nvme)
                console.log("nvme")
            }
            if (filtrosJSON.sata !== ''){
                this.where('sata', filtrosJSON.sata)
                console.log("sata")
            }
            if (filtrosJSON.frequencia !== ''){
                this.where('frequencia', filtrosJSON.frequencia)
                console.log("frequencia")
            }
            if (filtrosJSON.selo !== ''){
                this.where('selo', filtrosJSON.selo)
                console.log("selo")
            }
            if (filtrosJSON.link !== ''){
                this.where('link', filtrosJSON.link)
                console.log("link")
            }
        }
    ).catch((err) => { console.log( err); throw err })

    for (row of rows) {
        //  console.log(row)
    }

    
    // const rows = await knex.from('Hashrates').select("worker", knex.raw("date(date) AS date"))
    // .sum({hashsum: knex.raw('hashrate*interval')})
    // .where('date', '>=', from)
    // .where('date', '<=', to)
    // .groupByRaw('worker, date(date)')
    // .catch((err) => { console.log( err); throw err })

    // for (row of rows) {

    //     console.log(row)

    //     if (!result[row['date']]){
    //         result[row['date']] = {};
    //     }

    //     result[row['date']][row['worker']] = {"HashRateMedio": row['hashsum']/60/24}

    // }

    return rows;
}


module.exports = {listProd};