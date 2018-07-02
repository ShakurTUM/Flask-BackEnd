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

#Endpoint to input metadata
class metadata(Resource): 
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('filename', type=str, help='File Name')
			parser.add_argument('title', type=str, help='Title')
			parser.add_argument('description', type=str, help='Description')
			parser.add_argument('subject', type=str, help='subject')
			parser.add_argument('userId', type=str, help='userId')

			args = parser.parse_args()

			_filename = args['filename']
			_title = args['title']
			_description = args['description']
			_subject = args['subject']
			_user = args['userId']
			_userId = int(_user)

			newMetadata = Files(_filename, _title, _subject, _description, _userId)

			#print newMetadata
			db.session.add(newMetadata)
			db.session.commit()

			return jsonify('success')
		except Exception as e:
			return {'error': str(e)}