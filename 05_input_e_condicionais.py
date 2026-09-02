#coletar dados 
nome = input('Qual é o seu nome?\n')
print (f'eai {nome}, como você está?')
print( "insira sua data de nascimento")
dia = input ('Dia\n')
mes = input ('mes\n')
ano = input ('ano\n')
print (f'sua data de nascimento é {dia}/{mes}/{ano}')

#if elif /else
#se / se não se / se não
entrada = input('Você concorda com bolsonaro ? (sim/não)\n')
if entrada == 'sim':
    print('você é bolsonarista')
elif entrada == 'não':
    print('você não é bolsonarista')
else:
    print('Você ta fugindo da pergunta.')

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')

"""
Exercícios: Input e Condicionais

1. (Fácil) Solicite ao usuário que digite um número inteiro usando input(). Converta a resposta para int e verifique se o número é par (resto da divisão por 2 igual a 0), imprimindo a resposta apropriada usando if/else.
2. (Fácil) Crie um script que receba duas notas via input(), calcule a média entre elas, e classifique: se a média for >= 7 imprima 'Aprovado', se não 'Reprovado'.
3. (Médio - Misturando conceitos) Faça um programa que peça 3 lados de um triângulo (um por vez) usando input() e converta para float. Verifique com if/elif/else qual é o tipo de triângulo: Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (3 lados diferentes). (Dica: utilize os operadores lógicos e de comparação).
4. (Médio - Misturando conceitos) Peça ao usuário seu peso (kg) e altura (m). Calcule o IMC e mostre a classificação: Abaixo de 18.5 (Abaixo do peso), 18.5-24.9 (Normal), 25-29.9 (Sobrepeso) e >= 30 (Obesidade). Utilize f-strings para exibir o valor de IMC (com 2 casas decimais) e o status de forma estruturada.
5. (Complexo - Preparação Leetcode) Leap Year & Input Validation: Peça ao usuário um ano através de um input e converta para número inteiro. Implemente uma lógica de if/elif/else para determinar se o ano é Bissexto. Regras: um ano é bissexto se for divisível por 4, exceto aqueles divisíveis por 100, a menos que sejam também divisíveis por 400. Mostre a formatação exata indicando se o ano é bissexto ou não.
"""

