# json.decoder.JSONDecodeError
from json import JSONDecodeError
import json
import os


def read_json(filepath: str) -> list:
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)

    except (FileNotFoundError, JSONDecodeError):

        return create_json(filepath)


def create_json(filepath: str) -> list:

    with open(filepath, 'w') as json_file:
        json.dump({"data": []}, json_file, indent=2)
    
    return read_json(filepath)


def write_json(filepath: str, payload: dict):
    json_list = read_json(filepath).get("data")
    json_list.append(payload)

    with open(filepath, "w") as json_file:
        json.dump({"data": json_list}, json_file, indent=2)

    return payload



        

