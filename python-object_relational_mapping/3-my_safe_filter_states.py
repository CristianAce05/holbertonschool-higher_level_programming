#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument
in a way that is safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    # The %s is a placeholder, NOT string formatting.
    # The variable is passed as a tuple in the second argument.
    cur.execute("SELECT * FROM states WHERE name = %s \
                 ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
