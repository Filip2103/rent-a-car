from models.Db import Db
from datetime import datetime,timedelta

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

    def rent_car(self, user_id, car_id, days):
        con = self._get_connection()
        now = datetime.now()
        rented_until = now + timedelta(days=days)

        if self.if_rented(car_id, rented_until):
            raise ValueError("This car is already rented!")

        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO rent(user_id, car_id, rented_until,days) VALUES (%s, %s, %s, %s)",
            (user_id, car_id, rented_until,days)
        )
        con.commit()
        cursor.close()

        print("Rent successfully added to database!")

