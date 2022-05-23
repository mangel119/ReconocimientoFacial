import mysql.connector as db
import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root"
)

print(type(db))