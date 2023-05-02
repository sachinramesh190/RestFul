import os
import pandas as pd
from sqlalchemy import create_engine
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_cors import cross_origin
from flask import request
from flask import Blueprint
import userdomain as UserDomain
import argparse
user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.before_app_first_request
def create_users_table():
    print("Creating table")
    UserDomain.create_table()
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    args = parser.parse_args()
    if args.csv:
        UserDomain.delete_table()
        conn_string = f'mysql+pymysql://root:{os.getenv("db_root_password")}@{os.getenv("MYSQL_SERVICE_HOST")}/{os.getenv("db_name")}'
        engine = create_engine(conn_string)         
        df_users = pd.read_csv(args.csv)
        df_users.to_sql('Users', engine, index=False, if_exists='append')

@user_blueprint.route("/users", methods=["GET"])
@cross_origin()
def getAllUsers():
    """
    An API that returns details of all the users
    ---    
    responses:
        200:
            description: A list of users in the DB
            schema:
                id: users
                properties:
                    users:
                        type: list
                        description: List of admin users in the DB
                        default: None    
    """    
    users = UserDomain.get_all_users()
    if not users:
        return "Database exception", 500
    return {'users': users}, 200


@user_blueprint.route("/users", methods=['POST'])
@cross_origin()
def addUser():
    """
    An API that add a new user
    ---
    parameters:
       - name: user
         in: request
         type: string
         required: false       
    responses:
        200:
            description: Successfully added admin user
            schema:
                id: userId
                properties:
                    userId:
                        type: int
                        description: Autogenerated id the user created
                        default: None                
    """    
    name = request.json.get("name", None)
    if not name:
        return "User name is mandatory", 422
    id = UserDomain.add_user(name)
    return {'id': id}, 200


@user_blueprint.route("/users/<user_id>", methods=["GET"])
@cross_origin()
def getUser(user_id):
    """
    An API that returns admin user details using the JWT token
    ---
    responses:
        200:
            description: User details
            schema:
                id: user
                properties:
                    user:
                        type: dict
                        description: Details of the admin user
                        default: None    
    """    
    user = UserDomain.get_user_by_id(user_id)

    if not user:
        return "User does not exist", 404
    return user, 200