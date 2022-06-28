#importando bibliotacas random e time
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('Jogo do Jokenpô com o computador!')
print('''Escolha um para vencer o computador:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

#imput para usuario fazer sua jogada
print('-='*15)
jogador = int(input('Escolha uma das opções: '))
print('-'*20)

#sleep de 1s 
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(0.5)

#trazendo o resultado do jogador e do coputador
print('-'*20)
print('O computador escolheu: {}'.format(itens[computador].upper()))
print('Jogador escolheu: {}'.format(itens[jogador].upper()))
print('-='*15)

#validando a opcao escolhida pelo computador e suas variedades de resultados
if computador == 0: #cmoputador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('computador GANHOU')
elif computador == 1: # computador jogou pepel
    if jogador == 0:
        print('computador GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador GANHOU')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('jogador GANHOU')
    elif jogador == 1:
        print('computador GANHOU')
    elif jogador == 2:
        print('EMPATE')

