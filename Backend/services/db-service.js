
require('dotenv').config();
const fetch = require('node-fetch');
const dateformat = require('dateformat');

const DBoptions = {
    client: 'sqlite3',
    connection: {
        filename: "./../BD/main.sqlite"
    },
    useNullAsDefault: true
}



const knex = require('knex')(DBoptions);

async function listProd(tipo, compat) {
    console.log("Tipo: ", tipo)
    console.log("Compatibilidade: ", compat)

    const rows = await knex.from(tipo).select("site", "preco", "preco_desconto", "link", "nome")
    .catch((err) => { console.log( err); throw err })

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