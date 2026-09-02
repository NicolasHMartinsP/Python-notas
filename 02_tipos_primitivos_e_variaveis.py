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

"""
Exercícios: Tipos Primitivos e Variáveis

1. (Fácil) Declare variáveis para armazenar seu nome (str), idade (int), peso (float) e se possui um animal de estimação (bool). Imprima os tipos de cada variável usando a função type().
2. (Fácil) Crie uma variável recebendo uma string que contenha números (ex: "150"). Converta essa variável para inteiro e depois para float, imprimindo o resultado em cada etapa.
3. (Médio - Misturando conceitos) Faça a concatenação de uma variável string com o valor numérico de outra variável convertida para string, para formar a frase: "A idade de Maria é 25 anos".
4. (Médio - Misturando conceitos) Declare uma variável `saldo` com valor 100.50 (float) e `mensagem` com valor "Seu saldo atual é: ". Concatene e imprima o texto formatado corretamente (usando cast), e avalie através de uma expressão booleana se o saldo é maior que zero, guardando o resultado em uma variável `tem_saldo` para ser impressa também.
5. (Complexo - Preparação Leetcode) Escreva um pequeno bloco de código que realize um "swap" (troca) de valores entre duas variáveis (ex: a=5, b=10) sem usar uma terceira variável (pesquise sobre atribuição múltipla do Python) e verifique, com operadores booleanos, se os valores foram efetivamente trocados, imprimindo os booleanos resultantes da verificação.
"""

