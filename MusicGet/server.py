import socket

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def runServer():
    port = 9002

    app = make_app()
    app.listen(port)
    localIP = socket.gethostbyname(socket.gethostname())
    print("run in %s:%s" % (localIP, port))

    tornado.ioloop.IOLoop.current().start()
