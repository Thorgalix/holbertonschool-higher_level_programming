#!/usr/bin/python3
"""
This script safely filters states from the hbtn_0e_0_usa database by name
using parameterized queries to prevent SQL injection attacks.
It takes 4 arguments: mysql username, mysql password, database name,
and the state name to search for.
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
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s "
                   "ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
