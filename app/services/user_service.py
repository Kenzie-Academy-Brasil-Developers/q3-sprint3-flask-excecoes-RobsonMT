from app.services.json_handler import read_json


def verify_email(filepath: str, email: str) -> bool:
    database = read_json(filepath) 

    return [d for d in database["data"] if d["email"] == email]


def verify_values(args: dict) -> bool:

    if type(args["nome"]) != str or type(args["email"]) != str:
        
        return True
  