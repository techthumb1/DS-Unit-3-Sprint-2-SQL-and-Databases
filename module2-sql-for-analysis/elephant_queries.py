import psycopg2
# import sqlite3

DB_NAME = "ekasuicm"
DB_USER = "ekasuicm"
DB_PASSWORD = "5xL04dTyJuqjmPNeDPWsHjZsCnMmqpbM"
DB_HOST = "ruby.db.elephantsql.com"

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

cursor.execute('SELECT * from titanic_data;')

result = cursor.fetchall()
for row in result:
    print result
    print result[0]
    print result[1]
