from flask_restful import reqparse
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from flask_restful import Resource, Api
from .Users import Users
from resources.Users import db
from passlib.apps import custom_app_context as pwd_context

#Endpoint to make user

class userCreation(Resource): 
    def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('first_name', type=str, help='First name')
			parser.add_argument('last_name', type=str, help='Last name')
			parser.add_argument('dept_no', type=str, help='Department number')
			parser.add_argument('email', type=str, help='Email address to create user')
			parser.add_argument('password', type=str, help='Password to create user')
			args = parser.parse_args()

			_firstName = args['first_name']
			_lastName = args['last_name']
			_userEmail = args['email']
			_userPassword = args['password']
			_departmentNumber = args['dept_no']
			
			verification = Users.query.filter_by(email =_userEmail).first()

			#Unique emails
			if verification is not None:
				return jsonify('Email is already in use')

			# The custom_app_context object is an easy to use option 
			# based on the sha256_crypt hashing algorithm.

			_userPassword = pwd_context.encrypt(_userPassword) 

			newUser = Users(_firstName, _lastName, _departmentNumber, _userEmail, _userPassword)
			db.session.add(newUser)
			db.session.commit()
			return jsonify('success')
		except Exception as e:
			return {'error': str(e)}