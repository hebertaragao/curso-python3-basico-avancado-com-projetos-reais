# Operadores lógicos
# and (e) or (ou) not (nao)
# or Qualquer condição verdadeira avalia
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que você já viu)
# 0 0.0 "" False
# Também existe i tipo None que é 
# usado para representar um não valor.
entrada = input ('[E]entrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else: print('sair')

print(True or False or 0 or 'abc')
    