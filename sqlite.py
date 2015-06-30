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
        conn = sqlite3.connect("db/" + datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S') + ".db")
        print "Opened database successfully"

        conn.execute('''CREATE TABLE COMPANY
           (ID             INTEGER         PRIMARY KEY AUTOINCREMENT NOT NULL,
            HOST           VARCHAR(32)    NOT NULL,
            SERIAL         VARCHAR(32)    NOT NULL,
            STATUS         VARCHAR(32)    NOT NULL,
            TYPE           VARCHAR(32)    NOT NULL,
            AVAILABILITY   VARCHAR(32)    NOT NULL,
            BUILD          VARCHAR(32)    NOT NULL,
            TIMESTAMP      DATETIME       DEFAULT CURRENT_TIMESTAMP);''')

        print "Table created successfully"

    def close(self):
        conn.close()

if __name__ == "__main__":
    db = LogDatabase()
