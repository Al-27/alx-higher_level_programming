#!/usr/bin/python3
from sys import argv
import MySQLdb as sql

if __name__ == '__main__':
    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    
    connection = sql.connect("localhost", user, pwd, db, port=3306)
    cursor = connection.cursor()
    cursor.execute("select id, name from states order by id asc;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()