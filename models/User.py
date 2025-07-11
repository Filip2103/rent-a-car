from tkinter.font import names

from models.Db import Db
from faker import Faker
import random
faker=Faker()

class User(Db):

    names = [
        "Marko", "Nikola", "Ana", "Milica", "Luka",
        "Teodora", "Stefan", "Ivana", "Jovana", "Uroš"
    ]

    surnames = [
        "Jovanović", "Petrović", "Ilić", "Simić", "Nikolić",
        "Milenković", "Stanković", "Kovačević", "Popović", "Stojanović"
    ]


    def __init__(self):
        super().__init__()
        self.__name=None
        self.__age=None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):

        if len(name) < 5:
            raise ValueError("Name must be longer than 5 characters!")

        if len(name.split())<2:
            raise ValueError("Name must contain first and last name!")

        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):

        if age<18:
            raise ValueError("Age can't be under 18!")

        self.__age=age

    def create_user(self):

        if self.__name is None or self.__age is None:
            raise ValueError("Name and age must be set!")

        if self.user_exists():
            print(f"User '{self.__name}' already exists in the database.")
            return

        self.insert_user()
        print("User successfully added to database!")

    def insert_user(self):
        con = self._get_connection()

        cursor = con.cursor()
        cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)", (self.__name, self.__age))
        con.commit()
        cursor.close()



    def user_exists(self):
        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM user WHERE name=%s AND age=%s",(self.__name, self.__age))
        result=cursor.fetchone()

        return result['count']>0

    @classmethod
    def generate_user_name(cls):
        full_name = f"{random.choice(cls.names)} {random.choice(cls.surnames)}"
        return full_name

    @staticmethod
    def generate_age():
        return random.randint(18,65)


