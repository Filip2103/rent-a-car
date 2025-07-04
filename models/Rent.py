from math import radians

from models.Db import Db
from datetime import datetime,timedelta
import random
from faker import Faker
faker=Faker()

class Rent(Db):
    def __init__(self):
        super().__init__()

    def if_rented(self, car_id, rented_until):
        con = self._get_connection()
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM rent WHERE car_id=%s AND rented_until >= %s",
            (car_id, rented_until)
        )
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def rent_car(self, user_id, car_id, days, rented_at):
        con = self._get_connection()
        rented_until = rented_at + timedelta(days=days)

        # if self.if_rented(car_id, rented_until):
        #     raise ValueError("This car is already rented!")

        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO rent(user_id, car_id, rented_until,days,rented_at) VALUES (%s, %s, %s, %s, %s)",
            (user_id, car_id, rented_until,days,rented_at)
        )
        con.commit()
        cursor.close()

        print("Rent successfully added to database!")

    @staticmethod
    def generate_random_dob():
        dob=faker.date_between(start_date=datetime(2020,1,1), end_date=datetime(2024,12,31))
        return dob

    @staticmethod
    def generate_random_days():
        return random.randint(1,30)


    def generate_random_user_id(self):
        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("SELECT MAX(id) FROM user")
        result=cursor.fetchone()
        count = result['MAX(id)']

        return random.randint(1,count)

    def generate_random_car_id(self):
        con=self._get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT MAX(id) FROM car")
        result = cursor.fetchone()
        count=result['MAX(id)']

        return random.randint(1, count)

    def show_rents_per_year(self):
        con=self._get_connection()
        cursor=con.cursor()
        query= """
            SELECT YEAR(rented_at) AS `godina`, MONTHNAME(rented_at) AS `mesec`, COUNT(*) AS `broj_rentiranja`
            FROM rent
            GROUP BY YEAR(rented_at), MONTH(rented_at)
            ORDER BY YEAR(rented_at),MONTH(rented_at)

        """
        cursor.execute(query)
        data=cursor.fetchall()
        cursor.close()

        return data

    def show_rents_per_month(self):
        con=self._get_connection()
        cursor=con.cursor()

        query="""
            SELECT MONTHNAME(rented_at) AS `mesec`, COUNT(*) AS `broj_rentiranja`
            FROM rent
            GROUP BY MONTH(rented_at)
            ORDER BY MONTH(rented_at)
        """

        cursor.execute(query)
        data=cursor.fetchall()
        cursor.close()

        return data