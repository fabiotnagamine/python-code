from collections import defaultdict

class Grafo():
    def __init__(self):
        self.arestas = defaultdict(list)
        self.pesos = {}
    
    def adiciona_arestas(self, noInicial, noFinal, peso):
        self.arestas[noInicial].append(noFinal)
        self.arestas[noFinal].append(noInicial)
        self.pesos[(noInicial, noFinal)] = peso
        self.peso[(noFinal, noInicial)] = peso

def Djikstra (grafo, inicio, fim):
    caminhoCurto = {inicio : (None, 0)}
    noAtual = inicio
    visitado = set()

    while noAtual != fim:
        visitado.add(noAtual)
        destino = grafo.arestas[noAtual]
        pesoNodoAtual = caminhoCurto[noAtual][1]
        for proximoNo in destino:
            peso = grafo.peso[noAtual, proximoNo] + pesoNodoAtual
            if proximoNo not in caminhoCurto:
                caminhoCurto[proximoNo] = (noAtual, peso)
            else:
                current_shortest_weight = caminhoCurto[proximoNo][1]
                if current_shortest_weight > peso:
                    caminhoCurto[proximoNo] = (noAtual, peso)
        
        proximoDestino = {vertice: caminhoCurto[vertice]for vertice in caminhoCurto if vertice not in visitado}
        if not proximoDestino:
            return "Destino impossível de ser visitado!!!"
        noAtual = min(proximoDestino, key = lambda k: proximoDestino[k][1])
        caminho = []
        while noAtual is not None: 
            caminho.append(noAtual)
            proximoNo = caminhoCurto[noAtual][0]
            noAtual = proximoNo
            
        caminho = caminho[::-1]
        return caminho

grafo = Grafo()

arestas = [
    ("Oradea", "Zerind", 71),
    ("Oradea", "Sibiu", 151),
    ("Zerind", "Oradea", 71),
    ("Zerind", "Arad", 75),
    ("Arad", "Zerind", 75),
    ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118),
    ("Timisoara", "Arad", 118),
    ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Timisoara", 111),
    ("Lugoj", "Mehadia", 75),
    ("Mehadia", "Lugoj", 75),
    ("Mehadia", "Dobreta", 75), 
    ("Dobreta", "Mehadia", 75),
    ("Dobreta", "Craiova", 120),
    ("Craiova", "Dobreta", 120),
    ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138),
    ("Rimnicu Vilcea", "Sibiu", 80),
    ("Rimnicu Vilcea", "Craiova", 146)
    ("Rimnicu Vilcea", "Pitesti", 101),
    ("Sibiu", "Arad", 160),
    ("Sibiu", "Oradea", 151),
    ("Sibiu", "Fagaras", 99), 
    ("Fagaras", "Sibiu", 99),
    ("Fagaras", "Bucharest", 211),
    ("Pitesti", "Craiova", 138),
    ("Pitesti", "Rimnicu Vilcea", 97),
    ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Pitesti", 101),
    ("Bucharest", "Fagaras", 211), 
    ("Bucharest", "Urziceni", 85),
    ("Bucharest", "Giurgiu", 90),
    ("Giurgiu", "Bucharest", 90),
    ("Urziceni", "Bucharest", 85),
    ("Urziceni", "Vaslui", 142),
    ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Urziceni", 98),
    ("Hirsova", "Eforide", 86),
    ("Eforide", "Hirsova", 86),
    ("Vaslui", "Urziceni", 142),
    ("Vaslui", "Lasi", 92),
    ("Lasi", "Vaslui", 92),
    ("Lasi", "Neamt", 87),
    ("Neamt", "Lasi", 87)   
]

for aresta in arestas:
    grafo.adiciona_arestas(*aresta)

combinacoes = [
    ["Oradea", "Zerind"], ["Oradea", "Sibiu"],
    ["Zerind", "Oradea"], ["Zerind", "Arad"],
    ["Arad", "Zerind"], ["Arad", "Sibiu"], ["Arad", "Timisoara"],
    ["Timisoara", "Arad"], ["Timisoara", "Lugoj"],
    ["Lugoj", "Timisoara"], ["Lugoj", "Mehadia"], 
    ["Mehadia", "Lugoj"], ["Mehadia", "Dobreta"],
    ["Dobreta", "Mehadia"], ["Dobreta", "Craiova"],
    ["Craiova", "Dobreta"], ["Craiova", "Rimnicu Vilcea"], ["Craiova", "Pitesti"],
    ["Sibiu", "Oradea"], ["Sibiu", "Fagaras"], ["Sibiu", "Rimnicu Vilcea"],
    ["Rimnicu Vilcea", "Craiova"], ["Rimnicu Vilcea", "Pitesti"], ["Rimnicu Vilcea", "Sibiu"],
    ["Fagaras", "Sibiu"], ["Fagaras", "Bucharest"]
    ["Pitesti", "Rimnicu Vilcea"], ["Pitesti", "Craiova"], ["Pitesti", "Bucharest"],
    ["Bucharest", "Pitesti"], ["Bucharest", "Fagaras"], ["Bucharest", "Giurgiu"], ["Bucharest", "Urziceni"],
    ["Giurgiu", "Bucharest"], 
    ["Urziceni", "Bucharest"], ["Urziceni", "Hirsova"], ["Urziceni", "Vaslui"],
    ["Hirsova", "Eforide"], 
    ["Eforide", "Hirsova"],
    ["Vaslui", "Lasi"], ["Vaslui", "Urziceni"], 
    ["Lasi", "Vaslui"], ["Lasi", "Neamt"],
    ["Neamt", "Lasi"]
]

caminhosTotais = []

for i in range(len(combinacoes)):
    caminho = Djikstra(grafo, combinacoes[i][0], combinacoes[i][1])
    caminhosTotais.append(caminho)
    print("Caminho de "+ combinacoes[i][0] + " para " + combinacoes[i][1] + " : " )
    print(caminho)