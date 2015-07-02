#!/usr/bin/python

import tornado.ioloop
import tornado.web
import tornado.template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader("template/")
        self.write(str(loader.load("status.html").generate()))

application = tornado.web.Application([
    (r"/", MainHandler),
])

class WebServer():
    def  __init__(self, port=8888):
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()
        print "Web Server Launched and Stand-by Now."

if __name__ == "__main__":
    webserver = WebServer()
