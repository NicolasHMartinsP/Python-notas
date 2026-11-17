"""
Exercícios: Tipos Primitivos e Variáveis

1. (Fácil) Declare variáveis para armazenar seu nome (str), idade (int), peso (float) e se possui um animal de estimação (bool). Imprima os tipos de cada variável usando a função type().
2. (Fácil) Crie uma variável recebendo uma string que contenha números (ex: "150"). Converta essa variável para inteiro e depois para float, imprimindo o resultado em cada etapa.
3. (Médio - Misturando conceitos) Faça a concatenação de uma variável string com o valor numérico de outra variável convertida para string, para formar a frase: "A idade de Maria é 25 anos".
4. (Médio - Misturando conceitos) Declare uma variável `saldo` com valor 100.50 (float) e `mensagem` com valor "Seu saldo atual é: ". Concatene e imprima o texto formatado corretamente (usando cast), e avalie através de uma expressão booleana se o saldo é maior que zero, guardando o resultado em uma variável `tem_saldo` para ser impressa também.
5. (Complexo - Preparação Leetcode) Escreva um pequeno bloco de código que realize um "swap" (troca) de valores entre duas variáveis (ex: a=5, b=10) sem usar uma terceira variável (pesquise sobre atribuição múltipla do Python) e verifique, com operadores booleanos, se os valores foram efetivamente trocados, imprimindo os booleanos resultantes da verificação.
"""
#1 (Fácil)
Nome = input('Qual é o nome? \n')
Idade = input('Qual é a idade ? \n')
Peso = input('Qual é o peso? \n')
animal= input('Possui animal de estimação ? \n')
possui_animal = animal == 'sim'
print(f'{Nome}', type(Nome)) 
print(f'{Idade}',type(Idade))
print(f'{Peso}', type(Peso))
print(f'{possui_animal}', type(possui_animal))
#2 (Fácil)
Numeros = input('Insira um numero até 150 \n')
print(float(Numeros))
print(int(Numeros))
#3 (Médio)
nome_aluno = input('Insira o nome do aluno \n')
idade_aluno = input ('Insira a idade do aluno \n')
print(f'A idade de {nome_aluno}, é {idade_aluno}')
#4 (Médio)
