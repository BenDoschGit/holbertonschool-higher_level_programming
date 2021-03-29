#!/usr/bin/python3
""" Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the 4th argument.
protected from injection attacks.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if !(sys.argv[4].fid("\'")) and !(sys.argv[4].find('\"')):
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states \
                    Where name = %s \
                    ORDER BY id ASC", (sys.argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
