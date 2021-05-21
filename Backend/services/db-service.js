
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

async function listProd(tipo, filtros) {
    console.log("Tipo: ", tipo)
    console.log("Filtro: ", filtros)
    filtrosJSON = JSON.parse(filtros)
    console.log("JSON: ", filtrosJSON)

    var max_preco = min_preco = 0;

    const rows = await knex.from(tipo).select("*").where(
        function(){
            if (filtrosJSON.max_preco > 0){
                this.whereBetween('preco_desconto', [min_preco, max_preco])
            }
            if (typeof filtrosJSON.marca !== 'undefined') {
                this.where('marca', filtrosJSON.marca)
            }
            if (typeof filtrosJSON.chipset !== 'undefined'){
                this.where('socket', filtrosJSON.chipset)
            }
            if (typeof filtrosJSON.socket !== 'undefined'){
                this.where('socket', filtrosJSON.socket)
            }
            if (typeof filtrosJSON.tamanho !== 'undefined'){
                this.where('socket', filtrosJSON.tamanho)
            }
            if (typeof filtrosJSON.ddr !== 'undefined'){
                this.where('socket', filtrosJSON.ddr)
            }
            if (filtrosJSON.max_capacidade > 0){
                this.whereBetween('capacidade', [min_capacidade, max_capacidade])
            }
            if (filtrosJSON.max_frequencia > 0){
                this.whereBetween('frequencia', [min_frequencia, max_frequencia])
            }
            if (typeof filtrosJSON.cl !== 'undefined'){
                this.where('socket', filtrosJSON.cl)
            }
            if (filtrosJSON.max_vram > 0){
                this.whereBetween('vram', [min_vram, max_vram])
            }
            if (typeof filtrosJSON.fabricante !== 'undefined'){
                this.where('socket', filtrosJSON.fabricante)
            }
            if (typeof filtrosJSON.ssdhd !== 'undefined'){
                this.where('socket', filtrosJSON.ssdhd)
            }
            if (typeof filtrosJSON.potencia !== 'undefined'){
                this.where('socket', filtrosJSON.potencia)
            }
            if (filtrosJSON.max_potencia > 0){
                this.whereBetween('potencia', [min_potencia, max_potencia])
            }
            if (typeof filtrosJSON.selo !== 'undefined'){
                this.where('socket', filtrosJSON.selo)
            }
        }
    ).catch((err) => { console.log( err); throw err })

    for (row of rows) {

         console.log(row)

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