graph = {
   "Oradea": set(["Zerind", "Sibiu"]),
   "Zerind": set(["Arad", "Oradea"]),
   "Arad": set(["Zerind", "Sibiu", "Timisoara"]),
   "Sibiu": set(["Oradea", "Fagaras", "Arad", "Rimnicu_Vilcea"]),
   "Fagaras": set(["Sibiu", "Bucharest"]),
   "Timisoara": set(["Arad", "Lugoj"]),
   "Rimnicu_Vilcea": set(["Sibiu", "Craiova", "Pitesti"]),
   "Lugoj": set(["Timisoara", "Mehadia"]),
   "Pitesti": set(["Rimnicu_Vilcea", "Bucharest", "Craiova"]),
   "Mehadia": set(["Lugoj", "Dobreta"]),
   "Dobreta": set(["Mehadia", "Craiova"]),
   "Craiova": set(["Dobreta", "Rimnicu_Vilcea", "Pitesti"]),
   "Bucharest": set(["Pitesti", "Fagaras", "Giurgiu", "Urziceni"]),
   "Giurgiu": set(["Bucharest"]),
   "Urziceni": set(["Bucharest", "Hirsova", "Vaslui"]),
   "Hirsova": set(["Urziceni", "Eforie"]),
   "Eforie": set(["Hirsova"]),
   "Vaslui": set(["Urziceni", "Lasi"]),
   "Lasi": set(["Vaslui", "Neamt"]),
   "Neamt": set(["Lasi"])}
#queue é uma classe de fila sincronizada, implementa filas multiprodutoras e multiconsumidores


def bfs(graph, start):
   visitado, queue = [], [start]
   while queue:
       vertice = queue.pop(0)
       if vertice not in visitado:
           visitado.append(vertice) #anexa o item ao final da lista
           queue.extend(graph[vertice] - set(visitado)) #adiciona todos os elementos de um iterável ao final da lista
   return visitado


bfs(graph, "Arad")


def bfs_caminho(graph, start, goal):
   queue = [(start, [start])]
   while queue:
       (vertex, path) = queue.pop(0)
       for next in graph[vertex] - set(path):
           if next == goal:
               yield path + [next]
           else:
               queue.append((next, path + [next]))


list(bfs_caminho(graph, 'Oradea', 'Arad'))


def caminhoCurto(graph, start, goal):
   try:
       return next(bfs_caminho(graph, start, goal))
   except StopIteration:
       return None


print(caminhoCurto(graph, 'Lugoj', 'Bucharest'))

