// Representação do grafo como um objeto em JavaScript
let graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
};

console.log(graph["A"]["C"])

let nova = {}
for (let i in graph['A']) { 
    nova[i] = 2
    console.log(nova)
}

// Inicialização do objeto distances
// let distances = {};
// for (let node in graph) {
//     distances[node] = Infinity;
//     console.log(distances)
// }
// distances['A'] = 0;  // Supondo que 'A' é o nó inicial
