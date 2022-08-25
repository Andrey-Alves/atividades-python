    #   Palpites para a Mega Sena

from random import randint
from time import sleep

lista = []
jogos = []
quant = int(input('Quantos Jogos deseja sortear? '))
tot = 1  # Quando sortear os jogos, começar do 1, e não do 0
            # Fazendo assim contagem certa

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f'SORTEANDO {quant} JOGOS.')

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}') # i+1, para começar do 1 e não do 0
    sleep(1)  # Tempo entre um jogo e outro, 1 segundo
print('BOA SORTE !')