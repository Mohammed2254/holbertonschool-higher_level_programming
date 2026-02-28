#!/usr/bin/python3
"""Module for Selecting states with name starting with 'N'"""

import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                    ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
