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
    distance = {node:float('infinity') for node in graph}
    distance[start] = 0