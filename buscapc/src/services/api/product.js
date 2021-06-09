export function fetchProducts(query) {
    let filtro = JSON.stringify(query);
    return request({
        url: 'tipo=mobo&filtros=' + filtro,
        method: 'get',
    });
}