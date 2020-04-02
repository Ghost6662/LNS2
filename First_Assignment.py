print("----------------------------------Learn Python OOP with CleverProgrammer----------------------------------")
print("----------1st Part----------")

class Restaurant:
    def __init__(self, name, location, Price, Distance):
        self.name = name
        self.location = location
        self.Price = Price
        self.Distance = Distance


First_Restaurant = Restaurant('ABQ', 'Downtown', '$$$', 800)
Second_Restaurant = Restaurant('BBQ', 'Street 105', '$$', 100)

print('Name of First Restaurant is: ' + First_Restaurant.name)
print('Name of Second Restaurant is: ' + Second_Restaurant.name)

print('Location of First Restaurant is: ' + First_Restaurant.location)
print('Location of Second Restaurant is: ' + Second_Restaurant.location)

print('Price of First Restaurant is: ' + First_Restaurant.Price)
print('Price of Second Restaurant is: ' + Second_Restaurant.Price)

print('Distance to First Restaurant is: ' + str(First_Restaurant.Distance) + ' miles')
print('Distance to Second Restaurant is: ' + str(Second_Restaurant.Distance) + ' miles')

print('Distance btw 1st and 2nd Restaurant: ' + str(First_Restaurant.Distance - Second_Restaurant.Distance) + ' miles')

# Second Part
print("----------2nd Part----------")

class Course:
    website = "http://bestcourse.com"
    def __init__(self, name):
        self.name = name

Py_Course = Course("PY")
print(Py_Course.name)
print(Course.website)

print("----------3rd Part----------")

class StreetRace:
    def __init__(self, name):
        self.name = name
        self.pace = 100
        self.health = 100
        self.hit = 60
    def crash(self, racer):
        racer.pace = 0
        racer.health = racer.health - self.hit

First_Racer = StreetRace("Mike")
Second_Racer = StreetRace("Dany")

First_Racer.crash(Second_Racer)

print(Second_Racer.pace)
print(Second_Racer.health)

# Additional Self Part
print("----------Additional Self Part----------")
class Person:
    def __init__(self, name):
        self.name = name
        self.power = 100
        self.power_reduce = 30
        self.thirst = 100
        self.thirst_reduce = 40
        self.hunger = 0
        self.hunger_increase = 50
    def readbook(self,pers):
        pers.power = pers.power - self.power_reduce
        pers.thirst = pers.thirst - self.thirst_reduce
        pers.hunger = pers.hunger + self.hunger_increase
    def relax (self, pers):
        pers.power = 90
        pers.thirst = pers.thirst + 20
        pers.hunger = pers.hunger - 15

First_Reader = Person("Emil Eminov")

First_Reader.readbook(First_Reader)
print("----------After Reading----------")
print(First_Reader.name)
print(First_Reader.power)
print(First_Reader.thirst)
print(First_Reader.hunger)

First_Reader.relax(First_Reader)
print("----------After Relaxing----------")
print(First_Reader.name)
print(First_Reader.power)
print(First_Reader.thirst)
print(First_Reader.hunger)

print("----------4th Part----------")
class Person:
    def __init__(self, name):
        self.name = name
        self.power = 100
        self.power_reduce = 30
        self.thirst = 100
        self.thirst_reduce = 40
        self.hunger = 0
        self.hunger_increase = 50
        self.book_number = 200
    def __str__(self):
        return "Name:{} ->> Power:{}, Thirst:{}, Hunger:{}, Book Number:{}".format(self.name, self.power, self.thirst, self.hunger, self.book_number)
    def readbook(self,pers):
        pers.power = pers.power - self.power_reduce
        pers.thirst = pers.thirst - self.thirst_reduce
        pers.hunger = pers.hunger + self.hunger_increase
        pers.book_number -= 1
        print("After one reading session {} has {} power left, his thirst Level reduces to {}, Hunger level increases {}, and {} books left").format(self.name, self.power, self.thirst, self.hunger, self.book_number)
    def relax (self, pers):
        pers.power = 90
        pers.thirst = pers.thirst + 20
        pers.hunger = pers.hunger - 15
        print("After relaxing {}'s power increases to {} , his thirst Level increases to {}, Hunger level decreases {}").format(self.name, self.power, self.thirst, self.hunger)


First_Reader = Person("Emil Eminov")

print(First_Reader)
print ("\n")

First_Reader.readbook(First_Reader)
print(First_Reader)
print ("\n")

First_Reader.relax(First_Reader)
print(First_Reader)

