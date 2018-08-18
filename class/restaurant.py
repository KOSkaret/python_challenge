class Restaurant():
    """A simple model of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is serving " +
            self.cuisine_type + " to their customers.")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")

    def set_number_served(self, served):
        if self.number_served < served:
            self.number_served = served
        else:
            print("You can't serve less than you already have!")
    def increment_numer_served(self, served):
        if served < 0:
            print("Invalid number!")

        else:
            self.number_served += served

my_restaurant = Restaurant("bella","kebab")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("")
print("")
print("Second task")
# task 9-2
r1 = Restaurant("Pizzaria", "pizza")
r2 = Restaurant("Taco bell", 'taco')
r3 = Restaurant("McDonalds","burgers")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

#Task 9-4
print("")
print("")
print("Third task")
print(r3.number_served)
r3.set_number_served(29)
print(r3.number_served)
r3.increment_numer_served(10)
print(r3.number_served)
