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
    query = "SELECT cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id"
    cursor.execute(query)
    result = cursor.fetchall()

    new_row = [row[0] for row in result if row[1] == sys.argv[4].split("';")[0]]
    print(", ".join(new_row))

    cursor.close()
    db.close()
