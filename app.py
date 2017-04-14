from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from resources.Users import db
from resources.errors import errors


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:student33@localhost/Portal'
app.config.from_object('config')
api = Api(app, errors=errors, catch_all_404s=True)
db = SQLAlchemy(app)

#from resources.Users import Users
from resources.userCreation import userCreation
from resources.userDetails import userDetails
from resources.verifyUser import verifyUser

api.add_resource(userDetails, '/Users')
api.add_resource(userCreation, '/UserCreation')
api.add_resource(verifyUser, '/Login')

if __name__ == '__main__':
    app.run(debug=True)