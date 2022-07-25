graph = {
    "Oradea"          : ["Zerind", "Sibiu" ],
    "Zerind"          : ["Arad", "Oradea"], 
    "Arad"            : ["Zerind", "Timisoara", "Sibiu"],
    "Timisoara"       : ["Arad", "Lugoj"],
    "Lugoj"           : ["Timisoara", "Mehadia"],
    "Mehadia"         : ["Lugoj", "Dobreta"],
    "Dobreta"         : ["Mehadia", "Craiova"],
    "Craiova"         : ["Dobreta", "Rimnicu_Vilcea", "Pitesti"],
    "Rimnicu_Vilcea"  : ["Sibiu", "Craiova", "Pitesti"],
    "Pitesti"         : ["Craiova", "Rimnicu_Vilcea", "Bucharest"],
    "Sibiu"           : ["Arad","Oradea","Rimnicu_Vilcea", "Fagaras"],
    "Fagaras"         : ["Sibiu","Bucharest"],
    "Bucharest"       : ["Pitesti","Fagaras", "Urziceni", "Giurgiu"],
    "Giurgiu"         : ["Bucharest"],
    "Urziceni"        : ["Bucharest", "Vaslui", "Hirsova"],
    "Hirsova"         : ["Urziceni", "Eforide"], 
    "Eforide"         : ["Hirsova"],
    "Vaslui"          : ["Urziceni","Lasi"],
    "Lasi"            : ["Vaslui","Neamt"],
    "Neamt"           : ["Lasi"]   
}

def DLS(start,goal,path,level,maxD):
  print('\nProfundidade atual-->',level)
  print('Começo: ',start)
  path.append(start)
  if start == goal:
    print("Caminho atingindo")
    return path
  print('Caminho não atingido')
  if level==maxD:
    return False
  print('\nEspandindo o nó atual',start)
  for child in graph[start]:
    if DLS(child,goal,path,level+1,maxD):
      return path
    path.pop()
  return False
  
  
  
start = input('Cidade Inicial: ')
goal = input('Cidade Final:  ')
maxD = int(input("Profundidade máxima"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path to goal node available")
    print("Path",path)
else:
    print("No path available for the goal node in given depth limit")
            