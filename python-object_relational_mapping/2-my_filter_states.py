#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all records from the
'states' table where the name matches the provided argument, ordered by
their 'id' in ascending order.
The database credentials and name are provided as command-line arguments.
The results are printed to the console.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(sys.argv[4])
        )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
