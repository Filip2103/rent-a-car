from models.User import User
from models.Car import Car
from models.Rent import Rent

print("Options:"
      "\n1. Add user"
      "\n2. Add car"
      "\n3. Rent a car"
      "\n4. Show all cars"
      "\n5. Show rented cars")

available_option=[1,2,3,4,5]

option=None

while option is None:
    option=int(input("What option you want to do?"))

    if option not in available_option:
        raise ValueError("Unknown option!")

    if option == 1:
        user=User()
        user.name=input("Enter name:")
        user.age=int(input("Enter age:"))

        user.create_user()
        option=None

    elif option == 2:
        car=Car()
        car.brand=input("Enter brand:")
        car.model=input("Enter model:")

        car.create_car()
        option=None

    elif option == 3:
        rent=Rent()

        user_id=int(input("Enter user id:"))
        car_id=int(input("Enter car id"))
        days=int(input("How much days do you want to rent?"))

        rent.rent_car(user_id,car_id,days)
        option=None

    elif option == 4:
        car=Car()
        car.show_all_cars()
        option=None

    elif option == 5:
        car=Car()
        car.show_rented_cars()
        option=None