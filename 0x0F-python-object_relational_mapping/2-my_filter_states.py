#!/usr/bin/python3
""""that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches"""

import MySQLdb
import sys

def filter_state():
    """ that lists all states with a name starting with N
    Arguments:
        argv[0]: User name
        argv[2]: password
        argv[3]: Db name
        argv[4]: name searched
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd= sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states where name='{:s}' order by id asc".format(sys.argv[4]))

    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()

if __name__ == '__main__':
    filter_state()
