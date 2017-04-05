from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import SQLAlchemy

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
    #is_active = db.Column(db.Boolean, server_default="false", nullable=False)
	def __init__(self, firstname, lastname, departmentNumber, email, password):

 		self.first_name = firstname
   		self.last_name = lastname
   		self.dept_no = departmentNumber
   		self.email = email
   		self.password = password

	def __repr__(self):
		return '<User %r>' % self.first_name