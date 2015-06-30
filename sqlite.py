#!/usr/bin/python

import datetime
import os
import sqlite3
import time

class LogDatabase():

    def __init__(self):
        if not os.path.isdir("db/"):
            os.mkdir("db/")

        ts = time.time()
        self.conn = sqlite3.connect("db/" + datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S') + ".db")
        print "Opened database successfully"

        self.conn.execute('''CREATE TABLE LOG
           (ID             INTEGER         PRIMARY KEY AUTOINCREMENT NOT NULL,
            HOST           VARCHAR(32)    NOT NULL,
            SERIAL         VARCHAR(32)    NOT NULL,
            STATUS         VARCHAR(32)    NOT NULL,
            TYPE           VARCHAR(32)    NOT NULL,
            AVAILABILITY   VARCHAR(32)    NOT NULL,
            BUILD          VARCHAR(32)    NOT NULL,
            TIMESTAMP      DATETIME       DEFAULT CURRENT_TIMESTAMP);''')

        print "Table created successfully"
        self.cur = self.conn.cursor()

    def insert(self, host, serial, status, typ, availability, build):
        self.cur.execute("INSERT INTO log(host,serial,status,type,availability,build) VALUES('" + host + "', '" + serial + "', '" + status + "', '" + typ + "', '" + availability + "', '" + build + "')")
 
    def get_posts(self):
        self.cur.execute("SELECT * FROM LOG")
        print(self.cur.fetchall())

    def close(self):
        print "Closing database"
        self.conn.close()

if __name__ == "__main__":
    # This is a basic test for databse
    db = LogDatabase()
    for x in range(10):
        db.insert('a', 'a', 'a', 'a', 'a', 'a')
    db.get_posts()
    db.close()
