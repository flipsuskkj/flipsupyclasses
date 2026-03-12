dog = {'nome': 'roger', 'idade': '9', 'cor': 'verde'}

dog['comida favorita'] = 'carne'
print(list(dog.keys()))

del dog['cor']
print(dog)

