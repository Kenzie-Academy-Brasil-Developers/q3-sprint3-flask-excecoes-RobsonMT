from http import HTTPStatus
from flask import Flask, jsonify, request
import os

from app.decorators import verify_keys
from app.exceptions import EmailAlreadyExistError
from app.exceptions import RequestFormatError
from app.models.user import User


app = Flask(__name__)

DATABASE_FILEPATH = os.getenv("DATABASE_FILEPATH")

@app.get("/user")
def users():
    return jsonify(User.get_users()), HTTPStatus.OK


@app.post("/user")
@verify_keys()
def post_user():

    body_req = request.get_json()

    try:
        user = User(**body_req)
        return user.register_user(), HTTPStatus.CREATED
    except EmailAlreadyExistError as e:
        return {"error": e.message}, e.status_code
    except RequestFormatError as e:
        return {"wrong fields": e.message}, e.status_code