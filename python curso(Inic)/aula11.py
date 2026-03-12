
import argparse

parser = argparse.ArgumentParser(
    descrição = 'esse programa printa o nome dos meus cachorros'
)

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'vermelho', 'amarelo'}, help='a cor para procurar: ')


args = parser.parse_args()

print(args.color)