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
        self.count = 0
        self.written_books = 0
    def __str__(self):
        return "Name:{} ->> Power:{}, Thirst:{}, Hunger:{}, Book Number:{}".format(self.name, self.power, self.thirst, self.hunger, self.book_number)
    def readbook(self,pers):
        pers.power = pers.power - self.power_reduce
        pers.thirst = pers.thirst - self.thirst_reduce
        pers.hunger = pers.hunger + self.hunger_increase
        pers.book_number -= 1
        pers.count += 1
        print("After {} reading session {} has {} power left, his thirst Level reduces to {}, Hunger level increases {}, and {} books left").format(self.count, self.name, self.power, self.thirst, self.hunger, self.book_number)
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
print ("\n")

for i in range(1, 3):
    First_Reader.readbook(First_Reader)
    print(First_Reader)
    print ("\n")
First_Reader.relax(First_Reader)
print(First_Reader)
print ("\n")

print("----------5th Part----------")

class Writer(Person):
    def work(self):
        self.written_books += 1
        self.power = self.power - 50
        print("Written Book amount is {}").format(self.written_books)
        print("After {} writing session {} has {} power left, his thirst Level reduces to {}, Hunger level increases {}").format(self.written_books, self.name, self.power, self.thirst, self.hunger)


First_Writer = Writer("Dostoyevski")

First_Writer.work()
print("\n")
First_Writer.work()

First_Writer.relax(First_Writer)
print(First_Writer.power)
