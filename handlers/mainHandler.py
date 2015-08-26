__author__ = 'xiaobu'


import tornado.web as web


class MainHandler(web.RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        pass