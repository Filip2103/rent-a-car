from models.Db import Db


class User(Db):

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

        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("INSERT INTO user (name,age) VALUES (%s,%s)",(self.__name,self.__age))
        con.commit()
        cursor.close()

        print("User successfully added to database!")

    def user_exists(self):
        con=self._get_connection()

        cursor=con.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM user WHERE name=%s AND age=%s",(self.__name, self.__age))
        result=cursor.fetchone()

        return result['count']>0


