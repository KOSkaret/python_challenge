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


class IceCreamStand(Restaurant):
    """Represent the aspect of an restaurant, which are an ice
    cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes of parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self,flavor):
        self.flavors.append(flavor)
        print("The " + flavor + " was added to flavors")

    def show_flavors(self):
        print("\nWe have these flavors available:")
        for flavor in self.flavors:
            print(flavor)
