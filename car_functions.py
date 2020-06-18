def make_car(brand, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info