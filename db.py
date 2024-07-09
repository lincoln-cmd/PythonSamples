import mysql.connector as db_connector

host = '223.130.159.139'
database_name = 'test'
user = 'lincoln'
pwd = 'dong1515'


db_con = db_connector.connect(
    host=host,
    database=database_name,
    user = user,
    passwd = pwd
)

query = "SELECT * FROM tbl_usr"

print(db_con.is_connected())

#db_con.cursor().execute(query)

db_cursor = db_con.cursor()
db_cursor.execute(query)

result_set = db_cursor.fetchall()

print(result_set)

_id = 'test'
_pwd = 'asdf'
_name = 'fjfjfj'
_phone = '010-4534-1234'

query = 'INSERT INTO tbl_usr (id, pwd, name, phone) VALUES(%s, %s, %s, %s)'

val = (_id, _pwd, _name, _phone)

#db_con.cursor().execute(query)

db_cursor = db_con.cursor()
db_cursor.execute(query, val)
db_con.commit()