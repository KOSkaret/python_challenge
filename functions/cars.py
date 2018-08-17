def make_car(maker, model, **car_info):
    """Build a dictionary containing everything we know about the car."""
    car = {}
    car['maker'] = maker
    car['model'] = model

    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
