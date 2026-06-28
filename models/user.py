from flask_login import UserMixin

class User(UserMixin):


    def __init__(self, data):

        self.id = data["id"]
        self.username = data["username"]
        self.email = data["email"]
        self.password_hash = data["password_hash"]
        self.role = data["role"]

