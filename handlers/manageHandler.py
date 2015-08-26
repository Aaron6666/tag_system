__author__ = 'xiaobu'

from tornado import web as web


class ManageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("manage.html")

    def post(self, *args, **kwargs):
        pass