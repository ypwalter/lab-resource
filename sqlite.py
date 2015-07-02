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
           (ID             INTEGER        PRIMARY KEY AUTOINCREMENT NOT NULL,
            HOST           VARCHAR(32)    NOT NULL,
            SERIAL         VARCHAR(32)    NOT NULL,
            STATUS         VARCHAR(32)    NOT NULL,
            TYPE           VARCHAR(32)    NOT NULL,
            AVAILABILITY   VARCHAR(32)    NOT NULL,
            BUILD          VARCHAR(32)    NOT NULL,
            TIMESTAMP      DATETIME       DEFAULT CURRENT_TIMESTAMP);''')

        print "Table created successfully"
        self.cur = self.conn.cursor()

    def insert(self, host, serial, status, typex, availability, build):
        command = "INSERT INTO log(host,serial,status,type,availability,build) VALUES('" + host + "', '" + serial + "', '" + status + "', '" + typex + "', '" + availability + "', '" + build + "')"
        self.cur.execute(command)
        print command

    def get_log_all(self):
        self.cur.execute("SELECT * FROM log")
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def get_log_latest(self, number=1):
        self.cur.execute("SELECT * FROM log ORDER BY timestamp DESC LIMIT " + str(number))
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def get_log_latest_device(self, serial, number=5):
        self.cur.execute("SELECT * FROM log WHERE serial = '" + serial + "' ORDER BY timestamp DESC LIMIT " + str(number))
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def get_log_latest_all_devices(self):
        # SELECT * FROM log as l1 WHERE timestamp = (SELECT MAX(timestamp) FROM log as l2 WHERE l1.serial = l2.serial) GROUP BY serial
        self.cur.execute("SELECT id, host, log.serial, status, type, availability, build, log.timestamp FROM log INNER JOIN (SELECT serial, MAX(timestamp) AS mt FROM log GROUP BY serial) AS maxt ON log.serial = maxt.serial AND log.timestamp = maxt.mt")
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def get_log_latest_host(self, host, number=10):
        self.cur.execute("SELECT * FROM log WHERE host = '" + host + "' ORDER BY timestamp DESC LIMIT " + str(number))
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def get_log_latest_all_hosts(self):
        self.cur.execute("SELECT * FROM log as l1 WHERE timestamp = (SELECT MAX(timestamp) FROM log as l2 where l1.host = l2.host) GROUP BY host")
        ret = self.cur.fetchall()
        print(ret)
        return ret

    def close(self):
        print "Closing database"
        self.conn.close()

if __name__ == "__main__":
    # This is a basic test for database
    db = LogDatabase()
    for x in range(30):
        time.sleep(1)
        db.insert('1.1.1.' + str( (x+1) % 10 ), str( (x + 1) % 10 ), 'device', 'flame', 'available', 'build')
    print "Get the latest 1:"
    db.get_log_latest(1)
    print "Get the latest 2 for certain device:"
    db.get_log_latest_device("2", 2)
    print "Get the latest record for each device:"
    db.get_log_latest_all_devices()
    print "Get the latest 2 for certain host:"
    db.get_log_latest_host("1.1.1.1", 2)
    print "Get the latest record for each device:"
    db.get_log_latest_all_hosts()
    print "Get all log:"
    db.get_log_all()
    db.close()
