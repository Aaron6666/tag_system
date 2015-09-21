__author__ = 'xiaobu'

from tornado import web as web
from apps.signinService import SigninService

class SigninHandler(web.RequestHandler):
    def get(self):
        self.render("signin.html")

    def post(self, *args, **kwargs):
        service = SigninService()
        name = self.get_arguments("username")[0]
        psw = self.get_arguments("password")[0]
        print name
        print psw
        try:
            service.CheckOutUser(name,psw)
            self.set_cookie(name='username',value=name[0])
            self.render("index.html")
            print 1
        except:
            self.render("signin.html")
            print 2