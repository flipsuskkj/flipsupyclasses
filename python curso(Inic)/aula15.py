#polimorfismo sobrecarregamento de operador

class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

roger = dog('roger', 8)
syd = dog('syd', 7)
        
print(roger > syd)