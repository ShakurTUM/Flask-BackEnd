from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Users
from passlib.apps import custom_app_context as pwd_context

class makeAdmin(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('userId', type=str, help='userId')
			parser.add_argument('token', type=str, help='token')
			parser.add_argument('email', type=str, help='email of new admin')
			args = parser.parse_args()

			_userId = args['userId']
			_token = args['token']

			verification = Users.query.filter_by(UserId = _userId).first()

			# Only unique emails allowed
			if verification is not None and verification.is_active is not False: # Makes sure deleted accounts aren't allowed back in 
				auth = verification.verify_auth_token(_token)
				if auth is 'expired':
					return 'retry', 451
				elif auth is 'invalid':
					return 'bad token', 498
				else:
					 user = Users.query.filter_by(email=_userEmail).first()
					 if user is not None and user.is_active is not False:
					 	user.makeAdmin();
					 	return 'succes', 200 
					 else:
					 	return 'error: Wrong email', 409
			else:
				return 'incorrect creds' , 500
		except Exception as e:
			return {'error': str(e)}