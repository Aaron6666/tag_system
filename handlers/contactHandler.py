__author__ = 'xiaobu'


from tornado import web as web



class ContactHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("contact.html")


    def post(self, *args, **kwargs):
        pass
