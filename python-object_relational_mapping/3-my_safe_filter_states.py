#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ('%' + state_name + '%',))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
