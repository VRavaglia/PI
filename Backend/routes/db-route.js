const express = require('express');
const router = express.Router();
const dbService = require('../services/db-service')

router.get('/', async (req, res) => {
    const listOfProds = await dbService.listProd(req.query.tipo, req.query.filtros);
    res.status(200).send(listOfProds);
})

// router.get('/profit', async (req, res) => {
//     const profit = await dbService.calculateProfit();
//     res.status(200).send(profit);
// })

module.exports = router;