"""while/else"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
# Quando usado break dentro do while o else não é executado
        break

    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do while.')