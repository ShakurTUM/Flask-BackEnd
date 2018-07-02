from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

#Typical user

db = SQLAlchemy()

class Users(db.Model): # Had to match up name with database name
	UserId = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(250), nullable=False)
	last_name = db.Column(db.String(250), nullable=False)
	dept_no = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String(250), unique=True, nullable=False)
	password = db.Column(db.String(5000))
	creation_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
	is_active = db.Column(db.Boolean, server_default="false", nullable=False) # User is alive or deleted
	Privileges = db.Column(db.Boolean, server_default="false", nullable=False); # Deafult is normal user

	def __init__(self, firstname, lastname, departmentNumber, email, password):

 		self.first_name = firstname
   		self.last_name = lastname
   		self.dept_no = departmentNumber
   		self.email = email
   		self.password = password

   	def hash_password(self, password1):
   		self.password = pwd_context.encrypt(password1)

   	def makeAdmin(self):
   		self.Privileges = True
   	
   	def verify_password(self, password1):
   		return pwd_context.verify(password1, self.password)

	def __repr__(self):
		return '<User %r>' % self.first_name

	def generate_auth_token(self, expiration = 600):
		s = Serializer('SECRET_KEY', expires_in = expiration)
		return s.dumps({ 'Id': self.UserId })

	def activate(self):  # User signs up
		self.is_active = True
		self.Privileges = False

	def deactivate(self): # User decides to delete
		self.is_active = False


	@staticmethod
	def verify_auth_token(token):
		s = Serializer('SECRET_KEY')
		try:
			data = s.loads(token)
		except SignatureExpired:
			return 'expired' # valid token, but expired
		except BadSignature:
			return 'invalid' # invalid token
		#user = Users.query.get(data['UserId'])
		return 'Token is valid'


class Files(db.Model):
	fileId = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(250), nullable=True)
	title = db.Column(db.String(100), nullable=False)
	subject = db.Column(db.String(250), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	userId = db.Column(db.Integer, nullable=False)

	creation_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False);


	def __init__(self, filename, title, subject, description, userId):

		self.filename = filename
		self.title = title
 		self.subject = subject 
   		self.description = description
   		self.userId = userId

   	def __repr__(self):
		return '<Files %r>' % self.fileId

