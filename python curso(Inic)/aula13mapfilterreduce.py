#map()

numeros= [1,2,3]
def mapa():

    result = map(double = lambda a : a * 2, numeros)

    print(list(result))

#filter()

def filtro():
    numeros1= [1,2,3]
    def parouimpar(n):
        return n % 2 == 0

    resultado = filter(parouimpar, numeros1)

    print(list(resultado))

#reduce()
def reduzir():
    expenses = [
        ('Jantar', 80),
        ('Conserto do Carro', 120)
    ]

    sum = 0
    for expense in expenses:
        sum += expense[1]

    print(sum)