# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser
# verdadeiras
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy(que você já viu)
# 0 0.0 '' False
# também existe o tipo None que é
# usado para representar um valor
entrada = input ('[E]ntrada [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida: print('Entrar')
else: print('Sair')

print(True and True and True)
print(True and False and True)
print(True and 0 and True)
print(bool(0))
print(bool(0.0))
print(bool(''))
