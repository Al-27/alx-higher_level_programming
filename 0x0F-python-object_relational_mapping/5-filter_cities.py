#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
from sys import argv
import MySQLdb as sql

if __name__ == '__main__':
    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    srch = argv[4]
    query = f"SELECT cities.name FROM cities LEFT JOIN states ON states.id = cities.state_id WHERE states.name = '{srch}';"
    
    connection = sql.connect("localhost", user, pwd, db, port=3306)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cities = ""
    for row in results:
        cities += row[0] + ", "
        
    print(cities.strip(", "))
    cursor.close()
    connection.close()