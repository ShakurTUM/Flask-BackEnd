from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Users
from passlib.apps import custom_app_context as pwd_context

# Generate web token

class single(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('userId', type=str, help='Id')
			
			args = parser.parse_args()

			_userId = args['userId']
			
			verification = Users.query.filter_by(UserId=_userId).first()
			user = { 'id' : verification.UserId, 'name':verification.first_name + " " + verification.last_name, 'department' : verification.dept_no, 'email': verification.email }

			# Will be unique
			if verification is not None:
				return jsonify(users=user)
			else:
				return '', 404
		except Exception as e:
			return {'error': str(e)}
