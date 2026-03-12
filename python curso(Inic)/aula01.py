import random

def conseguir_escolhas():
    escolha_jogador = input('digite a sua escolha (pedra, papel, tesoura): ')
    options = ['papel', 'pedra', 'tesoura'] #essa lista diz para o random/a escolha do pc o que que ele tem de disponivel em seu arsenal
    escolha_pc = random.choice(options)
    escolhas = {'jogador' : escolha_jogador, 'pc' : escolha_pc}
    return escolhas

def quem_ganha(jogador, pc):
    #introdução aos condicionais
    print(f'você escolheu {jogador} e o PC escolheu {pc}')
    if (jogador == pc):
        return "é um empate!"
    elif jogador == 'pedra':
        if pc == 'tesoura':
            return 'pedra ganha de tesoura, você ganhou!!!'
        else:
            return 'papel ganha de pedra, VOCÊ perdeu'
    
    elif jogador == 'papel':
        if pc == 'pedra':
            return 'papel ganha de pedra, você ganhou!!!'
        else:
            return 'tesoura ganha de papel, VOCÊ perdeu'
    
    elif jogador == 'tesoura':
        if pc == 'papel':
            return 'tesoura ganha de papel, você ganhou!!!'
        else:
            return 'pedra ganha de tesoura, VOCÊ perdeu'

escolhas = conseguir_escolhas()
resultado = quem_ganha(escolhas['jogador'], escolhas['pc'])
print(resultado)