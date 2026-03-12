import random
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar()
class carta():
     def __init__(self, naipe, classe):
          self.naipe = naipe
          self.classe = classe

     def __str__(self):
          return f"{self.classe['classe']}  De {self.naipe}"
    

class Deck():
    def __init__(self):

        self.cartas = []
        naipes = ['Espadas', 'Paus', 'Copas', 'Ouros']
        classes = [
                {'classe': 'A', 'valor': 11},
                {'classe': '2', 'valor': 2},
                {'classe': '3', 'valor': 3},
                {'classe': '4', 'valor': 4},
                {'classe': '5', 'valor': 5},
                {'classe': '6', 'valor': 6},
                {'classe': '7', 'valor': 7},
                {'classe': '8', 'valor': 8},
                {'classe': '9', 'valor': 9},
                {'classe': '10', 'valor': 10},
                {'classe': 'J', 'valor': 10},
                {'classe': 'Q', 'valor': 10},
                {'classe': 'K', 'valor': 10},
            ]
        for naipe in naipes:
                    for classe in classes:
                        self.cartas.append(carta(naipe, classe))

    def embaralhar(self):
        if len(self.cartas) > 1:
            random.shuffle(self.cartas)

    
    def distribuir(self, numero):
        cartas_dadas = []

        for x in range(numero):
            if len(self.cartas) > 0:
                carta = self.cartas.pop()
                cartas_dadas.append(carta)
        return cartas_dadas
    
class mão():
    def __init__(self, dealer=False):
        self.cartas = []
        self.valor = 0
        self.dealer = dealer

    def add_carta(self, carta_list):
        self.cartas.extend(carta_list)
    
    def calcular_valor(self):
        self.valor = 0
        tem_as = False

        for carta in self.cartas:
             valor_carta = int(carta.classe['valor'])
             self.valor += valor_carta
             if carta.classe['classe'] == 'A':
                  tem_as = True

        if tem_as and self.valor > 21:
             self.valor -= 10

    def pegar_valor(self):
        self.calcular_valor()
        return self.valor
    
    def vinteeum(self):
        return self.Pegar_valor() == 21
    
    def mostrar(self, mostrar_cartas_dealer = False):
        print(f''' {"Dealer" if self.dealer else "Sua"} Mão: ''')
        for index, carta in enumerate(self.cartas):
            if index == 0 and self.dealer \
                and not mostrar_cartas_dealer and not self.vinteeum():
                print('Escondido')
            else:
                print(carta)

        if not self.dealer:
             print('valor:', self.pegar_valor())
        print()

class Jogo:
    def jogar(self):
        numero_jogo = 0
        jogos_pra_jogar = 0

        while jogos_pra_jogar <= 0:
            try: 
                 jogos_pra_jogar = int(input('Quantos Jogos Quer Jogar???: '))

            except:
                 print('você precisa colocar um número')
        
        while numero_jogo < jogos_pra_jogar:
            numero_jogo += 1

            deck = Deck()
            deck.embaralhar()

            player_hand = mão()
            dealer_hand = mão(dealer=True)

            for i in range(2):
                player_hand.add_carta(deck.distribuir(1))
                dealer_hand.add_carta(deck.distribuir(1))

            print()
            print('*' * 30)

            print(f'Jogo {numero_jogo} De {jogos_pra_jogar}')
            print('*' * 30)
            player_hand.mostrar()
            dealer_hand.mostrar()

            if self.check_venc(player_hand, dealer_hand):
                continue

            escolha = ''
            while player_hand.Pegar_valor() < 21 and escolha not in ['s', 'stand']:
                escolha = input('Hit or Stand?').lower()
                print()
                while escolha not in ['h', 's', 'hit', 'stand']:
                    escolha = input('Hit or Stand? (ou H/S)').lower()
                    print()
                if escolha in ['hit', 'h']:
                    player_hand.add_carta(deck.distribuir())
                    player_hand.mostrar()

            if self.check_venc(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.Pegar_valor()
            dealer_hand_value = dealer_hand.Pegar_valor()

            while dealer_hand_value < 17:
                dealer_hand.add_carta(deck.distribuir())
                dealer_hand_value = dealer_hand.Pegar_valor()

            if self.check_venc(player_hand, dealer_hand):
                continue

            print('resultados finais')
            print('Sua Mão:', player_hand_value)
            print('Sua Mão:', dealer_hand_value)

            self.check_venc(player_hand, dealer_hand, True)

    def check_venc(self, player_hand, dealer_hand, gameover=False):
            if not gameover:
                if player_hand.pegar_valor() > 21:
                    print('se passou hein. Dealer Venceu!')
                    return True
                elif dealer_hand.pegar_valor() > 21:
                    print('Dealer se passou hein. Player Venceu!')
                    return True
                elif player_hand.vinteeum() and player_hand.vinteeum():
                    print('Os Dois Fizeram 21, EMPATE!!!!')
                    return True
                if player_hand.vinteeum() > 21:
                    print('Vinte e um, Você venceu!!!')
                    return True
                if dealer_hand.vinteeum() > 21: 
                    print('Vinte e um, Você venceu!!!')
                    return True
                
            else:
                if player_hand.pegar_valor() > dealer_hand.pegar_valor():
                    print('você venceu!!')

                elif player_hand.pegar_valor() == dealer_hand.pegar_valor():
                    print('empate!!')

                else:
                    print('dealer ganhou....')
                return True
            return False
           

g = Jogo()
g.jogar()