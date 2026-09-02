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

"""
Exercícios: Formatação de Strings

1. (Fácil) Crie duas variáveis: `produto` = "Notebook" e `preco` = 3500.50. Imprima uma frase combinando-as usando f-string.
2. (Fácil) Usando o método `.format()`, formate uma string para exibir a frase "O {animal} tem {patas} patas.", passando argumentos nomeados.
3. (Médio - Misturando conceitos) Dado o valor `pi = 3.14159265`, utilize f-strings para imprimir este valor limitando a 3, a 4 e a 5 casas decimais (um em cada print).
4. (Médio - Misturando conceitos) Faça a divisão de 10 por 3, armazene o valor (float), e imprima-o formatado para exibir 4 casas decimais e com um símbolo de porcentagem no final usando f-strings. Depois, avalie se o valor é maior que 3 e inclua no mesmo f-string o resultado booleano dessa comparação.
5. (Complexo - Preparação Leetcode) Padding e Alinhamento: crie três variáveis com diferentes tamanhos de texto (`a='Id'`, `b='Nome'`, `c='Preço'`). Use formatação (seja f-strings ou `.format()`) para imprimir esses dados alinhados de forma que ocupe 5 espaços para a esquerda, 15 espaços centralizados e 10 espaços para a direita, gerando um cabeçalho de tabela perfeitamente estruturado, e na linha de baixo, simule os dados de um item para essa tabela usando o mesmo alinhamento de espaçamento.
"""

