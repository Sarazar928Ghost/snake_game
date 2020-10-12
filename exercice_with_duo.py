from enum import Enum


class Color(Enum):
    GREEN = [70, 220, 124]
    RED = [225, 26, 62]
    BLUE = [45, 151, 211]


class Animal:
    def __init__(self, color: Color):
        self.color = color


class Dog(Animal):
    def __init__(self, color: Color):
        super().__init__(color)


class Cat(Animal):
    def __init__(self, color: Color):
        super().__init__(color)


class Esperance:
    def __init__(self, variable):
        self.beau_bosse = variable
        print("Voilà tu m'as appelé :)")


ma_class = Esperance("Voilà je suis la variable envoyé")
print(ma_class.beau_bosse)

"""ma_variable = Cat()

animaux = [Dog(Color.GREEN), Cat(Color.RED), Dog(Color.BLUE), Cat(Color.GREEN)]
for animal in animaux:
    if isinstance(animal, Cat):
        print("Bon ok ... Je te l'accorde tu es un chat")
        print("Tu es de couleur ", animal.color.name)
    elif isinstance(animal, Dog):
        print("Bon ok ... Je te l'accorde tu es un bon toutou")
        print("Tu es de couleur ", animal.color.name)"""
