from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .Users import Users

class userDetails(Resource):
	def get(self):
		try:
			results = Users.query.all()
			json_results = []
			for result in results:
				d = {'Firstname':result.first_name, 'Lastname' : result.last_name}
				json_results.append(d)
			return jsonify(items=json_results)
		except Exception as e:
			return {'error' : str(e)}
