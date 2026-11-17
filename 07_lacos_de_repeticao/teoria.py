#loop infinito sem condição
condicao = True
while condicao:
    print(1)
    print(2)
    print(3)
# break pula o loop
contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)
print ('finalizou o loop')

qtd_linhas = 3 
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1
"""
for iterável -> str, range, etc (_iter_)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz'.__iter__()
textp = iter('Luiz') #mesma coisa que a de cima
print(texto)
##For/in

##range (start, stop, step)
numeros  = range(0, 100, 10)
for numero in numeros:
    print(numero)