print ('claudinho e bochecha')
# Isso é um comentário
"""
Isso é Docstring
"""
#\r\n -> CRLF
# \n -> LF
print("21","23","29","31","37", sep="-", end="\n") 

print('11','13','17','19', sep="-", end="\n")

print('2','3','5','7', sep="-", end="\n") #sep = separador end= quebra de linha 
# Tipos Primitivos
#string 
print('Olá, mundo!')
#Escape 
print('Olá, mundo!\nTudo bem?') #\n quebra linha
# ou utilize aspas simples para mostrar as aspas
print('olá mundo! "de boa ?"')
# r
print(r'Olá, mundo!\nTudo bem?')

#Float -> números Reais
print(3.14)
#Int -> Números Inteiros
print(10)
print (type(-7.22))
print (type(29))
print ( type('nico'))
#boolean
print(7.22 == 7)
print(28 == 28)
print(type(28 == 28))
print(type(28 == 'nico'))
#somas
print (1 + 1)
print ('a' + 'b')
print (float('1') + 1, type(float('1') + 1))
print (int('1') + 1, type(int('1') + 1))
print (bool(''))
print (bool(' '))

#PEP 8 biblioteca
#Váriaveis
nome_atleta = 'Kobe Bryant'
soma_cestas = 12 + 312
print(nome_atleta, soma_cestas)
int_1 = int('1')
print(int_1, type(int_1))
nome = 'Nico'
maior_idade = True
idade = 19
maior_de_idade = idade >= 18
print ("o", nome, "é maior de idade?", maior_de_idade)
#Operações
#adição
adição = 12 + 123.423
print('adição',adição, type(adição))
print(12 + 123)
#subtração
subtração = 12 - 123.423
print('subtração',subtração, type(subtração))
print(12 - 123)
#divisão
divisão = 10 / 3 #float
print('divisão',divisão, type(divisão))
divisão_inteira = 10 // 3 #int
print('divisão_inteira',divisão_inteira, type(divisão_inteira))
exponenciação = 2 ** 10
print('exponeciação',exponenciação, type(exponenciação))
modulo = 10 % 3
print('Modulo',modulo, type(modulo))
concatenacao = 'A' + 'B' + 'c'
print('Concatenacao',concatenacao, type(concatenacao))
a_dez = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez)
print(tres_vezes_luiz)
#Prioridade de operações
# 1- (n + n) 2- ** 3- * / // % 4- + -
conta = (1 + (2.5 - 1.5)) ** (5 + 5) 
print(conta)
nome = 'nico pepino'
altura = 1.73
peso = 75
imc = peso / altura ** 2
print (nome, 'possui a altura de', altura,'\nestá pesando', peso, 'logo seu imc é de')
print (imc)
# fstrings, é possui utilizar váriaveis dentro de uma string, utilizando {} para indicar a variável
texto1 = f'{nome} possui a altura de {altura} \nestá pesando {peso} logo seu imc é de \n {imc:.2f}'
print(texto1)
# Formatação de strings
c = 12.2423
a = 'Tulio'
b = 19
string = 'b={int} a={str} b={int} c={float:.2f}'
formato = string.format( str=a, int=b, float=c)
print(formato)
#coletar dados 
nome = input('Qual é o seu nome?\n')
print (f'eai {nome}, como você está?')
print( "insira sua data de nascimento")
dia = input ('Dia\n')
mes = input ('mes\n')
ano = input ('ano\n')
print (f'sua data de nascimento é {dia}/{mes}/{ano}')