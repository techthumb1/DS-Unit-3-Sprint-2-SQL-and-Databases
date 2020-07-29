import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic_data.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#query = f"""
#CREATE TABLE titanic_data (
#        id SERIAL PRIMARY KEY,
#        gender varchar,
#        age int4,
#        survived boolean
#);
#"""


insertion_query = f"""
INSERT INTO titanic_data (id, gender, age, survived)
VALUES ('7', '3', '9'),
       ('5', '2', '1'),
       ('9', '8', '7');
"""
#result = cursor.execute(query)
#print("RESULT", result)

#breakpoint()

#result2 = cursor.execute(query)
result3 = cursor.execute(insertion_query).fetchall()
#print("RESULT 2", result2)
print("RESULT 3", result3)
