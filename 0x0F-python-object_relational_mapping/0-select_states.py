#!/usr/bin/python3
""" Script that list all the state of the database hbtn_0e_0_usa """

import MySQLdb
import sys
def get_state() :
    """Get Ararment
    Arguments:
        argv[1]: mysql username
        arg[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("select * from states order by id ASC")

    rows = cursor.fetchall()

    for i in rows :
        print(i)

    cursor.close()
    db.close()

if __name__ == "__main__":
    get_state()