#!/usr/bin/python3
"""this lists all the states in the given database"""
import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    db.close()
