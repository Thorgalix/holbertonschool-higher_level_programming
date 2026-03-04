#!/usr/bin/env python3
"""
Lists all states starting with 'N' from hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        auth_plugin='mysql_native_password'
    )

    with db.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%'ORDER BY id ASC"
            )
        for row in cursor.fetchall():
            print(row)

    db.close()
