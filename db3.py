import mysql.connector as db_conn
import sqlite3

#2
'''host = '223.130.152.96'
db_name = 'mysqlite.db'
user = 'lincoln'
pwd = 'dong1515'

db_con = db_conn.connect(
    host = host,
    database = db_name,
    user = user,
    passwd = pwd
)'''

'''query = 'CREATE TABLE agent(no INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, agent_id CHAR(6) NOT NULL, agent_name CHAR(40) NOT NULL, working_area CHAR(35) NOT NULL, commission DECIMAL(10,2) NOT NULL, phone_no CHAR(15) NULL)'

db_cur = db_con.cursor()
db_cur.execute(query)
db_cur.close()'''

#3

'''query = "SELECT * FROM agent WHERE agent_id='test'"

db_cur = db_con.cursor()
db_cur.execute(query)
db_con.close()'''


#4

'''query = 'CREATE TABLE salesman(no INT AUTO_INCREMENT PRIMARY KEY, id INT(10) NOT NULL, name VARCHAR(20), location VARCHAR(20), num FLOAT(10))'

db_cur = db_con.cursor()
db_cur.execute(query)


query = ["INSERT INTO salesman(id, name, location, num) VALUES(5001,'James Hoog', 'New York', 0.15);",
          "INSERT INTO salesman(id, name, location, num) VALUES(5002,'Nail Knite', 'Paris', 0.25);",
          "INSERT INTO salesman(id, name, location, num) VALUES(5003,'Pit Alex', 'London', 0.15);",
          "INSERT INTO salesman(id, name, location, num) VALUES(5004,'Mc Lyon', 'Paris', 0.35);",
          "INSERT INTO salesman(id, name, location, num) VALUES(5005,'Paul Adam', 'Rome', 0.45);",
          ]

for i in query:
    db_cur = db_con.cursor()
    db_cur.execute(i)
    db_con.commit()

db_con.disconnect()'''


#5

host = '223.130.152.96'
db_name = 'TEST'
user = 'lincoln'
pwd = 'dong1515'

db_con = db_conn.connect(
    host = host,
    database = db_name,
    user = user,
    passwd = pwd
)

query = 'CREATE DATABASE IF NOT EXISTS TEST'

db_cur = db_con.cursor()
db_cur.execute(query)

rows = [(5001,'James Hoog', 'New York', 0.15), (5002,'Nail Knite', 'Paris', 0.25), (5003,'Pit Alex', 'London', 0.15), (5004,'Mc Lyon', 'Paris', 0.35), (5005,'Paul Adam', 'Rome', 0.45)]

query = 'CREATE TABLE IF NOT EXISTS test_table(no INT(10) AUTO_INCREMENT PRIMARY KEY, id INT(10) NOT NULL, name VARCHAR(20) NOT NULL, location VARCHAR(20) NOT NULL, num FLOAT(10) NOT NULL)'

db_cur = db_con.cursor()
db_cur.execute(query)

for i in rows:
    query = 'INSERT INTO test_table (id, name, location, num) VALUES (%s, %s, %s, %s)'
    val = (i[0], i[1], i[2], i[3])

    db_cur = db_con.cursor()
    db_cur.execute(query, val)
    db_con.commit()

db_con.disconnect()
