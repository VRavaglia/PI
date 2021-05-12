const express = require('express');
require('dotenv').config();
const cors = require('cors');

class App {
    constructor() {
        this.app = express();
        this.app.use(cors())
        this.routes();

        this.app.listen(3003, () => 
            console.log(`Escutando na porta http://localhost:3003`));

        
    }

    routes() {
        const dbRoute = require('./routes/db-route');
        this.app.use('/db', dbRoute);
    }
}

module.exports = new App().app;