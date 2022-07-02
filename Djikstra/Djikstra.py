#Biblioteca que classifica e acompanha os vértices que ainda não visitamos
from queue import PriorityQueue 

class Graph:
    def ___init___(self, numero_vertices):
        self.v = numero_vertices
        self.edges = [[-1 for i in range(numero_vertices)]for j in range (numero_vertices)]
        self.visited = []

    def add_edge(self, u, v, peso):
        self.edges[u][v] = peso
        self.edges[v][u] = peso
    
    def djikstra(grafo, verticeInicial):
        D = {v:float ('inf') for v in range (grafo.v)}
        D[verticeInicial] = 0

        pq = PriorityQueue()
        pq.put((0, verticeInicial))

        while not pq.empty():
            (distancia, verticeAtual) = pq.get()
            grafo.visited.append(verticeAtual)
            for vizinho in range(grafo.v):
                if grafo.edges[verticeAtual][vizinho] != -1:
                    dist = grafo.edges[verticeAtual][vizinho]
                    if vizinho not in grafo.visited:
                        custoAntigo = D[vizinho]
                        custoNovo = D[verticeInicial] + dist
                        if custoNovo < custoAntigo:
                            pq.put((custoNovo, vizinho))
                            D[vizinho] = custoNovo
        return D
"""
 Primeiro criamos uma lista D com tamanho v. A lista é onde manteremos os 
 caminhos mais curtos iniciando do vertice inicial para os outros nós
 Definimos um valor inicial como 0, pois essa é a distância dele mesmo.
 Em seguida iniciamos uma fila de prioridade, que é usada para classificar
 rapidamente os vértices do menos para o mais distante.
 O vértice inicial deve ser escolhido e colocado na lista de prioridade, para
 cada vértice visitado devemos marcá-lo, depois iterar com seus vizinhos
 Caso o vizinho não seja visitado, comparamos seus custos, caso a soma
 dos custos seja menor definimos como mais curto e atualizamos na fila 
"""

#Definindo os vertices eos vizinhos
g = grafo(0)
