__author__ = 'xiaobu'

from tornado import web as web
from apps.signinService import SigninService

class SigninHandler(web.RequestHandler):
    def get(self):
        self.render("signin.html")

    def post(self, *args, **kwargs):
        service = SigninService()
        name = self.get_arguments("username")
        psw = self.get_arguments("password")
        if service.CheckOutUser(name,psw):
            self.set_cookie(name='username',value=name)
            self.render("index.html")
        else:
            self.render("signin.heml")