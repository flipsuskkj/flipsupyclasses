#while, for - aula, não executar

condition = True
while condition == True:
    print('A Condição é verdadeira')
    condition = False

itens = [1,2,3,4]
for item in itens:
    print(item)

for item in range(15):
    print(item)

for index, item in enumerate(itens):
    print(index, item)


itens = [1,2,3,4]
for item in itens:
    if item == 2:
        continue
    print(item)