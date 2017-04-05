from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .Users import Users

class verifyUser(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('email', type=str, help='First name')
			parser.add_argument('password', type=str, help='Last name')

			_userEmail = args['email']
			_userPassword = args['password']

			# Only unique emails allowed
			verification = User.query.filter_by(email=_userEmail).first_or_404()
			if verifictation is 404 :
				return jsonify(Null)

			return pwd_context.verify(verification.password, _userPassword)

		except Exception as e:
			return {'error': str(e)}
