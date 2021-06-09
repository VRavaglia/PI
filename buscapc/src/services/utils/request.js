// Cria a instância do Axios
const service = axios.create({
    baseURL: 'http://localhost:3003/db',
    timeout: 10000, // Timeout
});

export default service;