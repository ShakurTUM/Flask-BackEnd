from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Portal'

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `Users` ("
    "  `UserId` int(11) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `dept_no` varchar(14) NOT NULL,"
    "  `email` varchar(50) NOT NULL,"
    "  `password` varchar(500) NOT NULL,"
    "  `creation_time` timestamp NOT NULL,"
    "  `is_active` tinyint NOT NULL,"
    "  `Privileges` tinyint NOT NULL,"
    "  PRIMARY KEY (`UserId`)"
    ") ENGINE=InnoDB")

TABLES['files'] = (
    "CREATE TABLE `files` ("
    "  `fileId` int(11) NOT NULL AUTO_INCREMENT,"
    "  `subject` varchar(250) NOT NULL,"
    "  `description` varchar(500) NOT NULL,"
    "  `filename` varchar(100) NOT NULL,"
    "  `title` varchar(100) NOT NULL,"
    "  `userId` int(11) NOT NULL,"
    "  `creation_time` timestamp NOT NULL,"
    "  PRIMARY KEY (`fileId`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='root', password='student33', host='127.0.0.1')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()