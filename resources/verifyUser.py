from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Users
from passlib.apps import custom_app_context as pwd_context
from flask import abort

class verifyUser(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('email', type=str, help='First name')
			parser.add_argument('password', type=str, help='Last name')
			args = parser.parse_args()

			_userEmail = args['email']
			_userPassword = args['password']
			verification = Users.query.filter_by(email=_userEmail).first()

			# Only unique emails allowed
			if verification is not None and verification.is_active is not False: # Makes sure deleted accounts aren't allowed back in 
				auth = verification.verify_password(_userPassword)
				if auth is True:
					authToken = verification.generate_auth_token()
					return jsonify(userId = str(verification.UserId), tokenString = str(authToken), privileges= str(verification.Privileges))
				elif auth is False:
					return 'error: Wrong password', 409
			else:
				return 'error: Wrong email', 409
		except Exception as e:
			return {'error': str(e)}
