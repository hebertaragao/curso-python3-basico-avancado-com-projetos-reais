"""
Listas em python
Tipo list Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
append, insert, pop, del, clear, extend, +
create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# print(lista[2])
# lista[2] = 300
# print(lista[2])
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop
print(lista, 'Removido', ultimo_valor)


