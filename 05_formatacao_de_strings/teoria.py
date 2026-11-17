# fstrings, é possui utilizar váriaveis dentro de uma string, utilizando {} para indicar a variável
nome = 'nico pepino'
altura = 1.73
peso = 75
imc = peso / altura ** 2

texto1 = f'{nome} possui a altura de {altura} \nestá pesando {peso} logo seu imc é de \n {imc:.2f}'
print(texto1)
# Formatação de strings
c = 12.2423
a = 'Tulio'
b = 19
string = 'b={int} a={str} b={int} c={float:.2f}'
formato = string.format( str=a, int=b, float=c)
print(formato)
