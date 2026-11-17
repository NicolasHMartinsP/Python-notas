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
