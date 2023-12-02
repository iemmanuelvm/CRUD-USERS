import csv
import os

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from Models import UserModel
from Schema import UserSchemaCreate, UserSchemaUpdate

blp = Blueprint("Users", "users", description="Operations CRUD on Users")

@blp.route("/user")

# READ AND CREATE USER
class UsersRC(MethodView):

    #
    @blp.response(201, UserSchemaCreate(many=True))

    # READ ALL USERS FROM DB
    def get(self):
        return UserModel.query.all()

    # CREATE USER IN DB
    @blp.arguments(UserSchemaCreate)
    @blp.response(201, UserSchemaCreate)
    def post(self, data_user):
        user_ = UserModel(**data_user)
        try:
            db.session.add(user_)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A user with that name email exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the user.")

        return user_
    
# DELETE AND UPDATE USER

@blp.route("/user/<string:user_id>")
class UserDU(MethodView):
    @blp.response(200, UserSchemaCreate)
    def get(self, user_id):
        user_ = UserModel.query.get_or_404(user_id)
        return user_

    def delete(self, user_id):
        store = UserModel.query.get_or_404(user_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "User deleted"}, 200


    @blp.arguments(UserSchemaUpdate)
    @blp.response(200, UserSchemaUpdate)
    def put(self, item_data, user_id):
        item = UserModel.query.get(user_id)

        if item:
            item.name        = item_data["name"]
            item.last_name   = item_data["last_name"]
            item.email       = item_data["email"]
            item.phone       = item_data["phone"]

        else:
            item = UserModel(id=user_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


