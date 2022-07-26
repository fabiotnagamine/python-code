import operator
from functools import reduce

# lista  = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# novaLista = map(lambda x, y: x * y, lista, lista2)
# print(list(novaLista))

# lista = [18,19,20,15,14,13,12,25,30,1,2,3,4,5,88,15,63,16,14,13,12,7]
# listaMaior = filter(lambda x: x > 12 , lista )
# print (list(listaMaior))

lista = [1,2,3,4]
soma  = reduce(operator.add, lista)
print(soma)

