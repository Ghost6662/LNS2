class Living_Being_Type:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def talk(self):
        pass
    def __str__(self):
        return "{} is a {}".format(self.name, self.type)
class Human(Living_Being_Type):
    def talk(self):
        return "Hello World!"
class Dog(Living_Being_Type):
    def talk(self):
        return "Woof!"
class Cat(Living_Being_Type):
    def talk(self):
        return "Meow!"


Emil = Living_Being_Type("Emil", "Human")
print (Emil)
print (Emil.talk())



EmilEminov = Human("Emil", "Human")
print(EmilEminov.talk())


Chasse = Dog("Chasse", "Dog")
print(Chasse.talk())

Chilli = Cat("Chilli", "Cat")
print(Chilli.type)
print(Chilli.talk())
print(Chilli)