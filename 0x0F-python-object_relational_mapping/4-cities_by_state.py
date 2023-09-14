#!/usr/bin/python3
import sys

import MySQLdb

db = MySQLdb.connect(
    host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
)

cursor = db.cursor()
query = "SELECT  * FROM cities"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)
cursor.close()
db.close()
