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