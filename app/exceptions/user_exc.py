class EmailAlreadyExistError(Exception):
    def __init__(
        self, message=None, status_code=409
    ) -> None:

        if not message:
            self.message = "User already exists."
        else:
            self.message = message

        self.status_code = status_code


class RequestFormatError(Exception):
    def __init__(self, nome: str, email: str, message=None, status_code=400
    ) -> None:

        if not message:
            if type(nome) != str:
                self.message = [{"nome": type(nome).__name__}]

            if type(email) != str:
                self.message = [{"email": type(email).__name__}]

            if type(nome) != str and type(email) != str:
                self.message = [{"nome": type(nome).__name__}, {"email": type(email).__name__}]
        
        else:
            self.message = message

        self.status_code = status_code