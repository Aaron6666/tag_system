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
            code,result = service.CheckOutUser(name,psw)
            if code == 1:
                self.set_cookie(name='username',value=name)
                self.render("index.html")
                print "ok"
            elif code==-1:
                print "no user"
                self.render("signin.html")
            else:
                print "wrong psw"
                self.render("signin.html")
        except:
            self.render("signin.html")
            print 2