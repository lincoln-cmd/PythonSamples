import requests
import mysql.connector as db_conn
import sqlite3
import time


host = '223.130.152.96'
db_name = 'mydatabase'
user = 'lincoln'
pwd = 'dong1515'


db_con = db_conn.connect(
    host=host,
    database=db_name,
    user=user,
    passwd=pwd
    )

query = 'SELECT * FROM mydatabase'

#print(db_con.is_connected())

urls=['https://temu.com', 'https://www.amazon.com/', 'https://ebay.com', 'https://alibaba.com']

while True:
    for url in urls:
        r = requests.get(url)
        _hash = str(hash(r.text))

        print('{}: {}'.format(url, _hash))

        query = 'INSERT INTO tbl_site_status_info (url, hash) VALUES (%s, %s)'
        val = (url, _hash)

        db_cur = db_con.cursor()
        db_cur.execute(query, val)
        db_con.commit()

    time.sleep(3)

db_con.disconnect()

