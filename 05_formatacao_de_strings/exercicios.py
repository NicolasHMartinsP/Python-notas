"""
Exercícios: Formatação de Strings

1. (Fácil) Crie duas variáveis: `produto` = "Notebook" e `preco` = 3500.50. Imprima uma frase combinando-as usando f-string.
2. (Fácil) Usando o método `.format()`, formate uma string para exibir a frase "O {animal} tem {patas} patas.", passando argumentos nomeados.
3. (Médio - Misturando conceitos) Dado o valor `pi = 3.14159265`, utilize f-strings para imprimir este valor limitando a 3, a 4 e a 5 casas decimais (um em cada print).
4. (Médio - Misturando conceitos) Faça a divisão de 10 por 3, armazene o valor (float), e imprima-o formatado para exibir 4 casas decimais e com um símbolo de porcentagem no final usando f-strings. Depois, avalie se o valor é maior que 3 e inclua no mesmo f-string o resultado booleano dessa comparação.
5. (Complexo - Preparação Leetcode) Padding e Alinhamento: crie três variáveis com diferentes tamanhos de texto (`a='Id'`, `b='Nome'`, `c='Preço'`). Use formatação (seja f-strings ou `.format()`) para imprimir esses dados alinhados de forma que ocupe 5 espaços para a esquerda, 15 espaços centralizados e 10 espaços para a direita, gerando um cabeçalho de tabela perfeitamente estruturado, e na linha de baixo, simule os dados de um item para essa tabela usando o mesmo alinhamento de espaçamento.
"""
#1 (Fácil)
produto = 'Notebook'
Preco = 3500.50
print('Confira aqui o preço do Notebook em oferta!')
print(f'{produto} = {Preco}')
#2 (Fácil)
animal = input('Registrar animal \n') 
patas = input('Quantidade de Patas \n')
cadastro = 'o {str} possui {int} patas.'
animal = cadastro.format(str=animal, int=patas)
print(animal) 
#3 (Médio)
pi = 3.14159265
decimal1 = f'{pi:.2}'
decimal2 = f'{pi:.3}'
decimal3 = f'{pi:.4}'
decimal4 = f'{pi:.5}'
decimal5 = f'{pi:.6}'
print(decimal1)
print(decimal2)
print(decimal3)
print(decimal4)
print(decimal5)
#4 (Médio)
divisao1 = 10 / 3
modulo = divisao1 > 3
print( f'qual é o resultado de 10/3 ? {divisao1:.4f} % e esse resultado é maior que 3 ? {modulo}')
#5 (Complexo)
id = 'ID'
produto = 'PRODUTO'
preço = "PREÇO"
item1 = input('Insira o seu sabor de açai para cadastrar \n')
iditem1 = input('qual o id do sabor ? \n')
precoitem1 = input('qual o valor do sabor ? \n')
print(f'|{id:<5}|{produto:^15}|{preço:>10}|')
print(f'|{iditem1:<5}|{item1:^15}|{precoitem1:>10}|')
