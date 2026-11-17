"""
Receba uma entrada de hora e volte uma confirmação de horário 6-11 bom dia 12-06 boa tarde 06-00 boa noite 00-6 vá dormir!
"""
horario = (input("Digite o horario atual por favor: "))
try:
   horario_int = int(horario)
   if 0 <= horario_int <= 6:
        print ("Vá dormir!")
   elif 7 <= horario_int <= 12:
        print ("bom dia")
   elif 13 <= horario_int <= 18:
        print ("Boa tarde!")
   elif 19 <= horario_int <= 23:
        print ("Boa noite!")
   else:print("digite apenas no ciclo de 24hrs")
except ValueError:
    print("por favor digite apenas numeros inteiros!")
"""
Receba uma entrada de nome que deve voltar um oi e reconhecer o tamanho do seu nome ex
4 letras olá (seu nome) é curto 6 letras olá seu nome é normal e +10 letras olá seu nome é enorme 
"""
nome = input("digite aqui seu nome por favor, eu quero muito saber: ").strip()
tamanho_nome = len(nome)

if tamanho_nome <= 1:
    print("por favor digite um nome maior")
elif tamanho_nome <= 4:
    print(f'Olá {nome} seu nome é bem curto ein')
elif tamanho_nome <= 10:
    print(f'Olá {nome} seu nome é bem normal')
else:
    print(f'Olá {nome} mas ai teu nome é enorme ein mn')
"""
tem que receber um numero inteiro e par, e informe se ele é par ou impar ou se ele não for um numero tem que avisar
"""
numero = input("por favor adicione qualquer numero inteiro: ")

try:
    numero_int = int(numero)
except ValueError:
    print("Por favor inserir um numero inteiro")
else:
    if numero_int % 2 == 0:
     print("esse numero é par!")
    else:
     print("esse numero é impar")

"""
faça uma calculadora com while e loops
"""
while True:
    valor = input('Digite um numero qualquer: ')
    operador = input('Digite qualquer operador basico: ')
    valor2 = input('Digite outro numero qualquer: ')
    valores_validos:None
    num_float = 0
    num2_float = 0
    try:
        num_float = float(valor)
        num2_float = float(valor2)
        valores_validos: True 
        
    except:
        valores_validos:None
        if valores_validos:None
        print('Digite apenas numeros inteiros por favor!')
        continue
    operadores = '+-/*'

    if operador not in operadores:
        print('Digite apenas operadores validos!')
    if len(operador) > 1:
        print('Por favor adicione um operador por vez')
        continue
    print('O resultado da conta é: ')
    if operador == '+':
        print(f'{num_float} + {num2_float} =', num_float + num2_float)
    elif operador == '/':
            print(f'{num_float} / {num2_float} =', num_float / num2_float)
    elif operador == '*':
            print(f'{num_float} * {num2_float} =', num_float * num2_float)
    elif operador == '-':
            print(f'{num_float} - {num2_float} =', num_float - num2_float)
    sair = input ('Gostaria de sair? [S]: ').lower().startswith('s')
    print(sair)
    if sair == True:
        break
##algoritmo para ler qual letra apareceu mais vezes em uma frase qualquer
frase = input('Adicione aqui uma frase qualquer: ')
i = 0
qtd_letra = 0
letra_comum = ''
   
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    letra_repetida = frase.count(letra_atual)
    if qtd_letra < letra_repetida:
        qtd_letra = letra_repetida
        letra_comum = letra_atual
    i+=1
print(
    'A letra que mais se repetiu foi '
    f'{letra_comum}, ela apareceu '
    f'{qtd_letra}x'
)

#faça um algoritmo que da uma palavra para o usuario adivinhar por letra
import os
incognita = 'pipoquinha'
acertos = ''
numero_tentativas = 0
while True:
    insert = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(insert) > 1:
        print('Digite apenas uma letra.')
        continue

    if insert in incognita:
        acertos += insert

        palavra_incognita = ''
    for letra_incognita in incognita:
        if letra_incognita in acertos:
            palavra_incognita += letra_incognita
        else:
            palavra_incognita += '*'

    print('A incognita era: ', palavra_incognita)

    if palavra_incognita == incognita:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Parabéns! você descobriu a palavra!')
        print('numero de tentativas: ', numero_tentativas)
        break