
from functools import wraps
from http import HTTPStatus
from typing import Callable
from flask import request


def verify_keys():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            trusted_keys = ["nome", "email"]
            body_keys = request.get_json()
            invalid_keys = set(trusted_keys).difference(body_keys)

            try:
                if invalid_keys:
                    raise KeyError({
                            "error": "wrong key(s)",
                            "expected": list(trusted_keys),
                            "received": list(body_keys),
                        })
                return func()
            except (KeyError , TypeError) as e:
                return e.args[0], HTTPStatus.BAD_REQUEST

        return wrapper   
    return decorator