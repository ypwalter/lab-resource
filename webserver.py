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

if __name__ == "__main__":
    print "Web Server Launched and Stand-by Now."
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
