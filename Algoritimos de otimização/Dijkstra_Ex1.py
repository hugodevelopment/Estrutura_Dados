# O algoritmo de Dijkstra é um método para encontrar o caminho mais curto entre dois pontos em um grafo. Aqui está uma explicação passo a passo:

# Inicialização: Começamos selecionando um nó inicial. Definimos a distância deste nó para si mesmo como 0 e a distância para todos os outros nós como infinito.
# Visitação: Visitamos todos os vizinhos do nó inicial e atualizamos suas distâncias. A distância de um nó é a soma da distância do nó inicial até o nó atual e o peso da aresta que conecta o nó atual ao seu vizinho.
# Atualização: Depois de visitar todos os vizinhos do nó inicial, escolhemos o nó com a menor distância que ainda não foi visitado. Este nó se torna nosso novo “nó atual”.
# Repetição: Repetimos os passos 2 e 3 até que tenhamos visitado todos os nós ou encontrado o nó de destino.
# Resultado: O resultado é o caminho mais curto do nó inicial ao nó de destino.
# Aqui está um exemplo visual de como o algoritmo funciona:

import heapq

def dijkstra(graph, start):
    # incialização
    #  Precisamos imitar essa configuração  Nó inicial: A
    # Nós: A(0), B(∞), C(∞), D(∞), E(∞)
    distances = {node:float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        # Escolha o nó com a menor distância acumulada
        current_distance, current_node = heapq.heappop(queue)

        # se a distancia atual for maior que  distancia acumulado do nós, pule para o próximo
        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

         # Se a distância através do nó atual for menor, atualize a distância do vizinho
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances 


# Exemplo de uso:
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 3), ('B', 2)]
}
print(dijkstra(graph, 'A'))

