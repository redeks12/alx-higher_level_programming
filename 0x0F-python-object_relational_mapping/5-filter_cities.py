#!/usr/bin/python3
import sys

import MySQLdb

db = MySQLdb.connect(
    host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
)

cursor = db.cursor()
query = (
    "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id"
)
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    if row[2] == sys.argv[4].split("';")[0]:
        print(row)
cursor.close()
db.close()
