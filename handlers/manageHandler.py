__author__ = 'xiaobu'

from tornado import web as web
from apps.showService import ShowService
import json

class ManageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        show = ShowService()
        list = show.allTags()
        name = [item[0].encode('utf-8') for item in list]
        print name
        self.render("manage.html",names =json.dumps(name))

    def post(self, *args, **kwargs):
        pass