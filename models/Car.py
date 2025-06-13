from models.Db import Db

class Car(Db):

    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004},
            {"model": "A5", "production_year": 2005},
            {"model": "A6", "production_year": 2006},
        ],
        "BMW": [
            {"model": "M4", "production_year": 2014},
            {"model": "M5", "production_year": 2015},
        ],
        "Mercedes": [
            {"model": "GLE", "production_year": 2024},
            {"model": "GLK", "production_year": 2025},
        ]
    }

    def __init__(self):
        super().__init__()
        self.__brand=None
        self.__model=None
        self.__production_year=None

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self,brand):
        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid brand!")

        self.__brand=brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self,model):
        if self.__brand is None:
            raise ValueError("Brand must be set!")

        valid_models=[]

        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car['model'])

        if model not in valid_models:
            raise ValueError("Invalid model!")

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model['model'] == model:
                self.__production_year = car_model['production_year']

        self.__model=model

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self,production_year):
        if self.__model is None:
            raise ValueError("Production year cannot be set!")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set!")

        self.__production_year=production_year

    def create_car(self):

        if self.__brand is None or self.__model is None or self.__production_year is None:
            raise ValueError("Brand,Model and production year must be set!")

        if self.car_exists():
            print(f"Car {self.__brand} {self.__model} already exists in database!")
            return

        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("INSERT INTO car (brand,model,production_year) VALUES (%s,%s,%s)",(self.__brand,self.__model,self.__production_year))
        con.commit()
        cursor.close()

        print("Car successfully added to database!")

    def car_exists(self):
        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM car WHERE brand=%s AND model=%s",(self.__brand,self.__model))
        result=cursor.fetchone()

        return result['count']>0

    def show_all_cars(self):
        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("SELECT * FROM car")
        results=cursor.fetchall()


        print(results)

    def show_rented_cars(self):
        con = self._get_connection()
        cursor = con.cursor()

        query = (
            "SELECT c.*, r.rented_until, "
            "CASE "
            "  WHEN TIMESTAMPDIFF(HOUR, NOW(), r.rented_until) < 24 THEN "
            "    CONCAT(TIMESTAMPDIFF(HOUR, NOW(), r.rented_until), ' sati') "
            "  ELSE "
            "    CONCAT(TIMESTAMPDIFF(DAY, NOW(), r.rented_until), ' dana') "
            "END AS preostalo_vreme "
            "FROM car AS c "
            "INNER JOIN rent AS r ON c.id = r.car_id "
            "WHERE r.rented_until >= NOW()"
        )

        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)
