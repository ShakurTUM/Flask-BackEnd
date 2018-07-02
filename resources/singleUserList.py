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

class singleList(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('userId', type=str, help='User id')
			args = parser.parse_args()

			_user = args['userId']
			_userId = int(_user)

			results = Files.query.filter_by(userId=_userId)

			json_results = []

			for result in results:
				file = { 'id' : result.fileId, 'filename' : result.filename, 'subject':result.subject, 'title':result.title, 'description' : result.description, 'uploadTime': result.creation_time, 'userId': result.userId }
				json_results.append(file)

			return jsonify(files=json_results)
		except Exception as e:
			return {'error' : str(e)}