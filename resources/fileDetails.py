from flask_restful import reqparse
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from flask_restful import Resource, Api
from .database import Files
from resources.database import db
from passlib.apps import custom_app_context as pwd_context
from flask import abort

#Endpoint to submit metadata

class userCreation(Resource): 
    def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('subject', type=str, help='Last name')
			parser.add_argument('description', type=str, help='Department number')
			args = parser.parse_args()

			_subject = args['subject']
			_description = args['description']

			if _subject is None or _description is None:
				abort(409)

			# The custom_app_context object is an easy to use option 
			# based on the sha256_crypt hashing algorithm.

			# _userPassword = pwd_context.encrypt(_userPassword) 

			newFile = Files( _subject, _description )

			db.session.add(newFile)
			db.session.commit()
			
			return jsonify('success')
		except Exception as e:
			return {'error': str(e)}