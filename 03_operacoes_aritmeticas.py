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

"""
Exercícios: Operações Aritméticas

1. (Fácil) Calcule e imprima o resto da divisão de 145 por 3 usando o operador de módulo (%).
2. (Fácil) Calcule o volume de um cubo cuja aresta mede 5 utilizando o operador de exponenciação (**).
3. (Médio - Misturando conceitos) Calcule as raízes de uma equação do 2º grau (Bhaskara) com a=1, b=-5, c=6, utilizando variáveis, exponenciação para raízes (ex: **0.5), e respeitando a prioridade de operações matemáticas. Imprima as raízes e seu tipo primitivo.
4. (Médio - Misturando conceitos) Uma loja aplica 15% de desconto em produtos. Crie uma variável com o preço original de R$ 250, aplique o cálculo matemático do desconto, armazene numa nova variável e imprima o resultado. Concatene strings e converta tipos para formatar a resposta na mesma linha de print.
5. (Complexo - Preparação Leetcode) Reverse Integer Concept: Dado um número inteiro positivo com 3 dígitos (ex: `num = 789`), utilize operações aritméticas sucessivas (divisão inteira `//` e módulo `%`) para extrair cada dígito individualmente (centena, dezena, unidade) e armazená-los em variáveis independentes. Depois, reconstrua o número de forma invertida (987) utilizando operações matemáticas e exiba o resultado.
"""
#1 (Fácil)
resto = 145 % 3
print (f'{resto}')
#2 (Fácil)
volume = 5 ** 3
print (f'o volume do cubo com lado de 5cm é {volume}')
#3 (Médio)
a = 1 
b = 5
c = 6
delta = (b**2) - 4*(a*c) #B^2 - 2 a.c
print(f'{delta}')
X1 =(-b + delta**0.5) / (2*a)
X2 =(-b - delta**0.5) / (2*a)
print (f'Esse é o valor de x1 {X1}', type(X1))
print (f'Esse é o valor de x2 {X2}', type(X2))
#4 (Médio)
produto1 = 250
produto_descontado = produto1 * (1 - 0.15)
print(produto_descontado)
print(f'o preço original do produto é {produto1} mas pagando a vista com desconto de 15% fica {produto_descontado}')
#5 (Complexo)
inteiro = input('Adicione o numero aqui para inverter ele\n')
ultimo_digito = int(inteiro) % 10
dezena = int(inteiro) // 10
digito_meio = dezena % 10
centena = int(inteiro) // 100
primeiro_digito = centena % 10
invertido = (ultimo_digito * 100) + (digito_meio * 10) + primeiro_digito
print(f'o numero invertido fica assim: {invertido}')