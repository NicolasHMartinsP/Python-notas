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
