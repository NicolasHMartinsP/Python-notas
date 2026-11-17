"""
Receba uma entrada de hora e volte uma confirmação de horário 6-11 bom dia 12-06 boa tarde 06-00 boa noite 00-6 vá dormir!
"""
horario = int(input("Digite o horario atual por favor: "))
 
if horario < 6:
    print ("Vá dormir!")
elif horario <= 12:
    print ("bom dia")
elif horario >= 18:
    print ("Boa tarde!")
else:
    print ("Boa noite!")

"""
Receba uma entrada de nome que deve voltar um oi e reconhecer o tamanho do seu nome ex
4 letras olá (seu nome) é curto 6 letras olá seu nome é normal e +10 letras olá seu nome é enorme 
"""

nome = (input("digite aqui seu nome por favor, eu quero muito saber: "))

tamanho_nome = len(nome)

if tamanho_nome <= 4:
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
