from models.User import User
from models.Car import Car
from models.Rent import Rent
from scripts.generate_multiple_users import generate_multiple_users
from scripts.generate_multiple_cars import generate_multiple_cars
from scripts.generate_multiple_rents import generate_multiple_rents
from scripts.visualize import visualize_rents_per_year,visualize_rents_per_month,visualize_rents_per_day


print("Options:"
      "\n1. Add user"
      "\n2. Add car"
      "\n3. Rent a car"
      "\n4. Show all cars"
      "\n5. Show rented cars"
      "\n6. Show earnings per car"
      "\n7. Insert random users"
      "\n8. Insert random cars"
      "\n9. Insert random rents"
      "\n10. Show rents per year"
      "\n11. Show rents per month"
      "\n12. Show the best weekday in the best month (SQL)"
      "\n13. Show the best weekday in the best month (DataFrame)"
      )

available_option=[1,2,3,4,5,6,7,8,9,10,11,12,13]

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
        car.price=int(input("Enter price:"))

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

    elif option == 6:
        car=Car()
        car.show_earnings_per_car()
        option=None
    elif option == 7:
        generate_multiple_users()
    elif option == 8:
        generate_multiple_cars()
    elif option == 9:
        generate_multiple_rents()
    elif option == 10:
        visualize_rents_per_year()
    elif option == 11:
        visualize_rents_per_month()
    elif option == 12:
        rent=Rent()
        print(rent.show_rents_per_day())
    elif option == 13:
        visualize_rents_per_day()