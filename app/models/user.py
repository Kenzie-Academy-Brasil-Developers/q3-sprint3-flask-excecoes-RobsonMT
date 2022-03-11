import os

from app.exceptions import EmailAlreadyExistError
from app.exceptions import RequestFormatError
from app.services import read_json
from app.services import write_json
from app.services import verify_email
from app.services import verify_values

class User:
    DATABASE_FILEPATH = os.getenv("DATABASE_FILEPATH")

    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email
        self.id = self.create_id()


    @staticmethod
    def create_id():
        return (User.length() + 1)


    @classmethod
    def get_users(cls):
        return read_json(cls.DATABASE_FILEPATH)


    @classmethod
    def length(cls):
        return len(cls.get_users().get("data"))


    def register_user(self):
        is_mal_formated = verify_values(self.__dict__)

        if is_mal_formated:
            raise RequestFormatError(self.nome, self.email)

        self.email = self.email.lower()
        
        already_exist_email = verify_email(self.DATABASE_FILEPATH, self.email)

        if already_exist_email:
            raise EmailAlreadyExistError()

        self.nome = self.nome.title()

        return write_json(self.DATABASE_FILEPATH, self.__dict__)