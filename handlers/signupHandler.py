__author__ = 'xiaobu'
#-*- coding:utf-8 -*-

from tornado import web as web
from apps.signupService import SignupService
from model import User
class SignupHandler(web.RequestHandler):
    """
    本类处理注册相关操作
    """
    def get(self):
        self.render("signup.html")

    def post(self, *args, **kwargs):
        #获取全部参数，类型是字典
        #{'username': ['1231'], 'password': ['123'], 'realname': ['1231'], 'email': ['1231']}
        #字典的value是列表，解析的时候需要注意
        ars = self.request.arguments
        service = SignupService()
        print ars
        service.signup(
            username=ars.get("username")[0],
            realname=ars.get("realname")[0].decode("utf-8"),
            password = ars.get("password")[0],
            email=ars.get("email")[0]
        )
        self.render("index.html")