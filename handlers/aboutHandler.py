__author__ = 'xiaobu'

import tornado.web as web

class AboutHandler(web.RequestHandler):
    def get(self):
        self.render("about.html")


    def post(self):
        pass