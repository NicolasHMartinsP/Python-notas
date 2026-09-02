# necessário criar ambiente
#Windows/Linux: python3 -m venv .venv
#ativar ambiente
#.venv\Scripts\Activate.ps1 windows
#source .venv/bin/activate Linux
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

"""
Exercícios: Print e Comentários

1. (Fácil) Escreva um programa que imprima o seu nome completo usando a função print(). Complete
2. (Fácil) Utilize a função print() com os argumentos `sep` e `end` para imprimir os números de 1 a 5 separados por uma barra invertida (\\) e terminando com dois pontos finais (..).
3. (Médio) Crie um script contendo comentários de linha (usando #) explicando o que cada print faz, e uma docstring no início do arquivo descrevendo o objetivo geral do script.
4. (Médio) Imprima a matriz identidade de ordem 2 (2x2) usando prints sucessivos, alinhando os números perfeitamente e alterando o separador entre as colunas para um espaço ou tabulação (\t).
5. (Complexo - Preparação Leetcode) Imagine que você está escrevendo a função de saída para um tabuleiro de jogo da velha. Escreva uma sequência de `print`s utilizando `sep` (como '|') e `end` adequadamente para desenhar o tabuleiro inicial vazio (3x3), apenas com espaços ou hífens no lugar das peças.
"""

#1 (Fácil)
nome = input('Digite aqui seu nome completo por favor\n')
print(f'Seu nome completo é {nome}')
#2 (Fácil)
print( "1","2","3","4","5", sep ="\\", end="..\n") 
#3 (Médio)
"""
O objetivo do script é fazer um comparativo numerico entre dois inputs
"""
#esse input recebe um valor qualquer
primeiro_valor = input('Digite aqui um numero qualquer da seguencia anterior \n')
segundo_valor = input('Digita aqui o segundo numero qualquer \n')
#esse outro recebe a segunda condição
if primeiro_valor == segundo_valor: #esse if compara os dois inputs
    print('os numeros são iguais') #esse print retorna a comparação se for true
else: 
    print('os numeros são diferentes negão') #esse aqui retorna se for false
#4 (Médio)
Numero_1x1 = input('insira o numero da primeira linha da matrix 2x2 \n')
Numero_2x1 = input('insira o numero da segubda linha da matrix 2x2 \n')
Numero_1x2 = input('insira o numero da terceira linha da matrix 2x2 \n')
Numero_2x2 = input('insira o numero da quarta linha da matrix 2x2 \n')
print('A sua matrix 2x2 está pronta, confira aqui:')
print(f'{Numero_1x1}, \t {Numero_2x1}')
print(f'{Numero_1x2}, \t {Numero_2x2},')
#5 (Complexo)
print('-','-','-', sep="|", end="\n")
print('-','-','-', sep="|", end="\n")
