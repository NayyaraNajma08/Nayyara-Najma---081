def make_car(manufacturer, model, **car_info):
    """Return a dictionary of information about a car."""
    car = {"manufacturer": manufacturer, "model": model}
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car("Subaru", "outback", color="blue", tow_package=True)
print()
print(car)