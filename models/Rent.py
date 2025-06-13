from models.Db import Db
from datetime import datetime,timedelta

class Rent(Db):
    def __init__(self):
        super().__init__()

    def rent_car(self,user_id,car_id,days):
        con=self._get_connection()
        now=datetime.now()
        rented_until = now + timedelta(days=days)

        cursor=con.cursor()
        cursor.execute("SELECT * FROM rent WHERE car_id=%s AND rented_until >= %s",(car_id,rented_until))

        if cursor.fetchone():
            raise ValueError("This car is already rented!")

        cursor.execute("INSERT INTO rent(user_id,car_id,rented_until) VALUES (%s,%s,%s)",(user_id,car_id,rented_until))
        con.commit()
        cursor.close()

        print("Rent successfully added to database!")
