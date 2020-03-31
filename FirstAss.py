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

print('Distance between First and Second Restaurant: ' + str(First_Restaurant.Distance - Second_Restaurant.Distance) + ' miles')
