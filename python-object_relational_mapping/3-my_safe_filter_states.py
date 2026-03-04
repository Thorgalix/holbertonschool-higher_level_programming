#!/usr/bin/python3
"""
This script lists all states from the hbtn_0e_0_usa database that match
the name provided as an argument, sorted by their id in ascending order.
It takes 4 arguments: mysql username, mysql password, database name,
and the state name to search for. The results are printed as tuples.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    # Build SQL query using parameterized query
    cursor.execute("SELECT * FROM states WHERE name = %s "
                   "ORDER BY id ASC", (sys.argv[4],))

    # Print rows exactly as tuples
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
