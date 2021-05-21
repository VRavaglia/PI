
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

    console.log("Filtros utilizados:")

    const rows = await knex.from(tipo).select("*").where(
        function(){
            if (filtrosJSON.max_preco > 0){
                this.whereBetween('preco_desconto', [min_preco, max_preco])
                console.log("preco")
            }
            if (typeof filtrosJSON.marca !== 'undefined') {
                this.where('marca', filtrosJSON.marca)
                console.log("marca")
            }
            if (typeof filtrosJSON.chipset !== 'undefined'){
                this.where('socket', filtrosJSON.chipset)
                console.log("chipset")
            }
            if (typeof filtrosJSON.socket !== 'undefined'){
                this.where('socket', filtrosJSON.socket)
                console.log("socket")
            }
            if (typeof filtrosJSON.tamanho !== 'undefined'){
                this.where('tamanho', filtrosJSON.tamanho)
                console.log("tamanho")
            }
            if (typeof filtrosJSON.ddr !== 'undefined'){
                this.where('ddr', filtrosJSON.ddr)
                console.log("ddr")
            }
            if (filtrosJSON.max_capacidade > 0){
                this.whereBetween('capacidade', [filtrosJSON.min_capacidade, filtrosJSON.max_capacidade])
                console.log("capacidade - min/max")
            }
            if (typeof filtrosJSON.capacidade !== 'undefined'){
                this.where('capacidade', filtrosJSON.capacidade)
                console.log("capacidade")
            }
            if (filtrosJSON.max_quantidade > 0){
                this.whereBetween('quantidade', [filtrosJSON.min_quantidade, filtrosJSON.max_quantidade])
                console.log("quantidade - min/max")
            }
            if (typeof filtrosJSON.quantidade !== 'undefined'){
                this.where('quantidade', filtrosJSON.quantidade)
                console.log("quantidade")
            }
            if (filtrosJSON.max_frequencia > 0){
                this.whereBetween('frequencia', [filtrosJSON.min_frequencia, filtrosJSON.max_frequencia])
                console.log("frequencia")
            }
            if (typeof filtrosJSON.frequencia !== 'undefined'){
                this.where('frequencia', filtrosJSON.frequencia)
                console.log("frequencia")
            }
            if (typeof filtrosJSON.cl !== 'undefined'){
                this.where('socket', filtrosJSON.cl)
                console.log("cl")
            }
            if (filtrosJSON.max_vram > 0){
                this.whereBetween('vram', [filtrosJSON.min_vram, filtrosJSON.max_vram])
                console.log("vram")
            }
            if (typeof filtrosJSON.vram !== 'undefined'){
                this.where('vram', filtrosJSON.vram)
                console.log("vram")
            }
            if (typeof filtrosJSON.fabricante !== 'undefined'){
                this.where('socket', filtrosJSON.fabricante)
                console.log("socket")
            }
            if (typeof filtrosJSON.ssdhd !== 'undefined'){
                this.where('ssdhd', filtrosJSON.ssdhd)
                console.log("ssdhd")
            }
            if (filtrosJSON.max_potencia > 0){
                this.whereBetween('potencia', [filtrosJSON.min_potencia, filtrosJSON.max_potencia])
                console.log("potencia")
            }
            if (typeof filtrosJSON.potencia !== 'undefined'){
                this.where('potencia', filtrosJSON.potencia)
                console.log("potencia")
            }
            if (typeof filtrosJSON.selo !== 'undefined'){
                this.where('selo', filtrosJSON.selo)
                console.log("selo")
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