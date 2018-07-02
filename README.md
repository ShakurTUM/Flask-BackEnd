# Back-End
Flask RESTful backend 


## Installation
This installation guide is for use on your own server, realistically users will interact with the application through the web requiring no installation from users.
 
There are several components to install. For the portal’s components to run several python packages need to be installed  as well as nodejs. For the the python packages install through pip using the command: 
- sudo pip install -r requirements.txt 

The text file contains the necessary packages.
 
Firstly a database is needed, and a database called ‘Portal’. Using the python script Database_Setup.py with your config, the database setup is complete (using MySQL database). From the diagram below you can make out my config for the MySQL database in the mysql.connecter, change the connecter based on your config.


![alt text](https://github.com/lennono/Flask-BackEnd/blob/master/pics/Database.png)


After the script is run the tables will be created with the columns in the above image. 
 
After the database is setup, the python backend can be initialised. The backend has been constructed in such a way that the only command needed is python app.py to run the app's entry point. After the command is run the server should be running as


![alt text](https://github.com/lennono/Flask-BackEnd/blob/master/pics/Python_server.png)

 


