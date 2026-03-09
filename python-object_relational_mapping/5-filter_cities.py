#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    # Join cities and states, filtering by the state name parameter
    cur.execute("""SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = cur.fetchall()
    # Extract names from tuples and join them with commas
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()
