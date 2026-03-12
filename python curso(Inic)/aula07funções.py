import time
while True:
    nome = str(input('Qual é o seu nome?: '))
    idade = int(input('Qual é a sua Idade?: '))

    def ola(nome):
        if nome != str:
            print('isso não pode ser seu nome. tente novamente em 5 segundos')
            print(5)
            time.sleep(1)
            print(4)
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
        else:
            print(f'Olá, {nome}!')
            checkidade()


    def checkidade(idade):
        if idade >= 18:
            print('você é um adulto')
        elif idade >= 12:
            print('você é um adolescente')
        else:
            print('você é uma criança')

    ola(nome)
    break