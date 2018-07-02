from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from passlib.apps import custom_app_context as pwd_context
from .database import Files
import zipfile
import boto
import boto.s3.connection
from boto.s3.key import Key
import werkzeug

class upload(Resource):
   	def post(self):
   		try:

   			# Amazon s3 Config
   			access_key = 'AKIAJIZCGRMWJ6QJZINA'
			secret_key = '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'

			conn = boto.connect_s3(aws_access_key_id = access_key, 
				aws_secret_access_key = secret_key)

			bucket = conn.get_bucket('adaptcentre')

	   		parse = reqparse.RequestParser()
	   		parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
	   		
	   		args = parse.parse_args()
	   		File = args['file']
	   		contents = File.read()


	   		response = []
	   		files = []
	   		keys = []
	   		zipped = False
	   		count = 0

	   		# Sort zip files
	   		if zipfile.is_zipfile(File) is True:
	   			zipped = True
	   			z = zipfile.ZipFile(File)
	   			if z.testzip() is not None:
	   				return {'error': 'Bad zip'}, 400

	   			for filename in z.namelist():
	   				keys.append(filename)
	   				files.append(z.read(filename))

	   		# Upload Single files 
	   		if zipped is False:
	   			f = { 'filename' : File.filename }
	   			response.append(f)

	   			key = bucket.new_key(File.filename)
	   			key.set_contents_from_string(contents)	   		
	   		
	   		# Upload Zip files 
	   		else:
	   			for filename in keys:
	   				f = { 'filename' :filename }
	   				response.append(f)
	   				content = files[count]
	   				count = count + 1
	   				key = bucket.new_key(filename)
	   				key.set_contents_from_string(content)

	   		return jsonify(filnames=response)
	   	except Exception as e:
				return {'error': str(e)}
   		