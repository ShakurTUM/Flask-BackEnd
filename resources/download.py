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
import boto
import sys, os
from boto.s3.key import Key


class download(Resource): 
    def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('filename', type=str, help='File to be downloaded')
			
			args = parser.parse_args()
			_filename = args['filename']

			AWS_ACCESS_KEY_ID = 'AKIAJIZCGRMWJ6QJZINA'
			AWS_SECRET_ACCESS_KEY = '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'

			bucket_name = 'adaptcentre'

			# Connect to the bucket
			conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
			bucket = conn.get_bucket(bucket_name)
			
			k = Key(bucket)
			k.key = _filename

			plans_key = bucket.get_key(_filename)
			plans_url = plans_key.generate_url(3600, query_auth=True, force_http=True)
			
			return jsonify(filedownload=plans_url)
			
		except Exception as e:
			return {'error': str(e)}