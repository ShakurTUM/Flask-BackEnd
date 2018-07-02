from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from resources.database import db
from resources.errors import errors
from flask_restful.utils import cors
from flask_cors import CORS, cross_origin
#from sendgrid import *




app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000/*"}}, supports_credentials=True)
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:student33@localhost/Portal'
app.config.from_object('config')
api = Api(app, errors=errors, catch_all_404s=True)
db = SQLAlchemy(app)

#from resources.Users import Users
from resources.userCreation import userCreation
from resources.userDetails import userDetails
from resources.verifyUser import verifyUser
from resources.getAuth import getAuth
from resources.verifyToken import verifyToken
from resources.makeAdmin import makeAdmin 
from resources.upload import upload 
from resources.metadata import metadata
from resources.getfiles import getFiles
from resources.download import download
from resources.single import single
from resources.singleUserList import singleList

api.add_resource(userDetails, '/Users')
api.add_resource(userCreation, '/UserCreation')
api.add_resource(verifyUser, '/Login')
api.add_resource(getAuth, '/auth')
api.add_resource(verifyToken, '/token')
api.add_resource(makeAdmin, '/admin')
api.add_resource(upload, '/upload')
api.add_resource(metadata, '/metadata')
api.add_resource(getFiles, '/files')
api.add_resource(download, '/download')
api.add_resource(single, '/single')
api.add_resource(singleList, '/UserUploads')

if __name__ == '__main__':
    app.run(debug=True)