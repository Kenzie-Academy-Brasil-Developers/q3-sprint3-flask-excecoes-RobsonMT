from http import HTTPStatus
from flask import Flask, jsonify, request
import os

from app.models.user import User


app = Flask(__name__)

DATABASE_FILEPATH = os.getenv("DATABASE_FILEPATH")


@app.get("/user")
def users():
    return jsonify(User.get_users()), HTTPStatus.OK

@app.post("/user")
def post_user():

    body_req = request.get_json()

    user = User(**body_req)

    return user.register_user(), HTTPStatus.CREATED