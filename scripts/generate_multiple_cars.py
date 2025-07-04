from models.Car import Car


def generate_multiple_cars(count=20):

    for i in range(count):
        car=Car()
        car.brand, car.model = Car.generate_brand()
        car.production_year=Car.generate_production_year()
        car.price=Car.generate_price()
        car.create_car()