from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Files
from flask_restful.utils import cors

class getFiles(Resource):
	def get(self):
		try:
			results = Files.query.all()
			json_results = []
			for result in results:
				file = { 'id' : result.fileId, 'filename' : result.filename, 'subject':result.subject, 'title':result.title, 'description' : result.description, 'uploadTime': result.creation_time, 'userId': result.userId }
				json_results.append(file)
			return jsonify(files=json_results)
		except Exception as e:
			return {'error' : str(e)}
