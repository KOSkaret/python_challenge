from restaurant import Restaurant

r1 = Restaurant("Pizzaria", "pizza")

r1.describe_restaurant()
print(r1.number_served)
r1.set_number_served(29)
print(r1.number_served)
r1.increment_numer_served(10)
print(r1.number_served)
