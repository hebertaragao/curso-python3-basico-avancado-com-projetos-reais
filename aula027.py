"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento[i:f:p][::]
Obs.: a função len retorna a qtde
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:8])
print(variavel[0:5])
print(variavel[:6])
print(variavel[-8:-2])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[::-1])
print(variavel[-1:-10:-1])