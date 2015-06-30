#!/usr/bin/env python

import socket, threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "New thread started for " + self.ip + ":" + str(self.port)

    def run(self):    
        print "Connection from - " + self.ip + ":" + str(self.port)

        self.socket.send("<< Control Server Connected >>\n")
        data = "0"

        while len(data):
            data = self.socket.recv(1024)
            print "Client " + self.ip + ":" + str(self.port) + " sent - " + data
            self.socket.send(data + " received.\n")

        print "Client " + self.ip + ":" + str(self.port) + " disconnected."

host = "localhost"
port = 10054

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []

while True:
    tcpsock.listen(20)
    print "Server Initialed on " + host + ":" + str(port)
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)
    
for t in threads:
    t.join()
