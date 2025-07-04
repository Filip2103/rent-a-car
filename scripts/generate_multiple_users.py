from models.User import User

def generate_multiple_users(count=50):

    for i in range(count):
        user=User()
        user.name=User.generate_user_name()
        user.age=User.generate_age()
        user.create_user()

