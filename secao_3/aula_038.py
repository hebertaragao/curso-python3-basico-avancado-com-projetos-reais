"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtde_linhas = 5
qtde_colunas = 5

linha = 1
while linha <= qtde_linhas:
    coluna = 1
  
    while coluna <= qtde_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')