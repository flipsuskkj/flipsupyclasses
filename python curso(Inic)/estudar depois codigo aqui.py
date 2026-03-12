import random
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar()

cartas = []
naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']
classes = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q' ,'K']

def embaralhar():
    random.shuffle(cartas)

for naipe in naipes:
    for classe in classes:
        cartas.append([naipe, classe])
        

def distribuir(numero):
    cartas_dadas = []
    
    for x in range(numero):
        carta = cartas.pop()
        cartas_dadas.append(carta)
    return cartas_dadas


embaralhar()

cartas_dadas = distribuir(2)
carta = cartas_dadas[0]
classe = carta[1]

if classe == 'A':
    valor = 11

elif classe == 'K' or classe == 'Q' or classe == 'J':
    valor = 10

else:
    valor = classe

classe_dict = {'classe': classe , 'valor': valor}
print(classe_dict['classe'], ['valor'])