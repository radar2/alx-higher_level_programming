#!/usr/bin/python3
""""that lists all states with a name starting with N"""
import MySQLdb
import sys

def filter_state():
    """ that lists all states with a name starting with N
    Arguments:
        argv[0]: User name
        argv[2]: password
        argv[3]: Db name
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd= sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states where name like binary 'N%' order by id asc")

    rows = cursor.fetchall()

    for i in rows:
        print(i)
    cursor.close()
    db.close()

if __name__ == '__main__':
    filter_state()
