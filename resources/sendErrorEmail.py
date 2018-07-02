from flask import jsonify
from flask_restful import reqparse, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from .Users import Users
from passlib.apps import custom_app_context as pwd_context
import sendgrid
import os
from sendgrid.helpers.mail import *

class sendErrorEmail(Resource): 
    def get(self):
    	try:
    		#SENDGRID_API_KEY='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'
    		print 'here'
    		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))
    		from_email = Email("owen.lennon4@mail.dcu.ie")
    		to_email = Email("owenlennon3@gmail.com")
    		subject = "Sending with SendGrid is Fun"
    		content = Content("text/plain", "and easy to do anywhere, even with Python")
    		mail = Mail(from_email, subject, to_email, content)
    		response = sg.client.mail.send.post(request_body=mail.get())
    		print(response.status_code)
    		print(response.body)
    		print(response.headers)
    	except Exception as e:
    		return {'error': str(e)}