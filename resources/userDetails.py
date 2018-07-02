from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .database import Users
from flask_restful.utils import cors

class userDetails(Resource):
	def get(self):
		try:
			results = Users.query.all()
			json_results = []
			for result in results:
				user = { 'id' : result.UserId, 'name':result.first_name + " " + result.last_name, 'department' : result.dept_no, 'email': result.email }
				json_results.append(user)
			return jsonify(users=json_results)
		except Exception as e:
			return {'error' : str(e)}
