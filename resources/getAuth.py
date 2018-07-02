from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Users
from passlib.apps import custom_app_context as pwd_context

# Generate web token

class getAuth(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('id', type=str, help='Id')
			args = parser.parse_args()

			_userId = args['id']
			verification = Users.query.filter_by(UserId=_userId).first()

			# Will be unique
			if verification is not None:
				auth = verification.generate_auth_token()
				return auth, 200
			else:
				return '', 404
		except Exception as e:
			return {'error': str(e)}
