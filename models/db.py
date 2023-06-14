from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#instance = 'sqlite:///restaurant'
instance = 'mysql+pymysql://Farmville:123@/Farmville?unix_socket=/run/mysqld/mysqld.sock'
#instance = "mysql+pymysql://Farmville:123@localhost:3306/Farmville"

