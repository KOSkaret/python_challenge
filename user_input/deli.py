sandwich_orders = ["Egg Tomato and Scallion Sandwich", "Funeral Sandwiches",
    "Grilled Deli Sandwiches", "Hot Ham and Cheese Croissant"]
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("I made your " + current_order)

    finished_sandwiches.append(current_order)

for sandwich in finished_sandwiches:
    print(sandwich)
