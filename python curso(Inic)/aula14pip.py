#pip & list comressions

numeros = [1,2,3,4,5]

numeros_power_2 = [n**2 for n in numeros]

print(numeros_power_2)

numeros_power_2 = []
for n in numeros:
    numeros_power_2.append(n**2)

numeros_power_2 = list(map(lambda n : n**2, numeros))