from app.services import read_json, write_json
import os


class User:
    # DATABASE_FILEPATH = "app/database/database.json"
    DATABASE_FILEPATH = os.getenv("DATABASE_FILEPATH")

    def __init__(self, nome: str, email: str):
       self.nome = nome.capitalize()
       self.email = email.lower()
       self.id = self.create_id()


    # Create new_id
    @staticmethod
    def create_id():
        return (User.length() + 1)

    # get users
    @classmethod
    def get_users(cls):
        return read_json(cls.DATABASE_FILEPATH)


    # User lenght
    @classmethod
    def length(cls):
        return len(cls.get_users().get("data"))

    # register new_user
    def register_user(self):
        return write_json(self.DATABASE_FILEPATH, self.__dict__)