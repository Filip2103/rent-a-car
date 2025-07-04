from models.Rent import Rent

def generate_multiple_rents(count=10000):

    for i in range(count):
        rent=Rent()
        user_id=rent.generate_random_user_id()
        car_id=rent.generate_random_car_id()
        days=Rent.generate_random_days()
        rented_at=Rent.generate_random_dob()
        rent.rent_car(user_id,car_id,days,rented_at)