"""
Iterável -> str, range, etc(__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#texto = iter('Hebert') # __iter__()
#print(next(texto)) # __next__()
#print(texto.__next__()) 
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

texto = 'Hebert' #iterável
iteratador = iter(texto) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break



