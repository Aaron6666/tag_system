__author__ = 'xiaobu'
#-*- coding:utf-8 -*-

from tornado import web as web
from apps.signupService import SignupService
from model import User
class SignupHandler(web.RequestHandler):
    def get(self):
        self.render("signup.html")

    def post(self, *args, **kwargs):
        #获取全部参数，类型是字典
        #{'username': ['1231'], 'password': ['123'], 'realname': ['1231'], 'email': ['1231']}
        #字典的value是列表，解析的时候需要注意
        ars = self.request.arguments
        service = SignupService()
        service.signup(
            username=ars.get("username"),
            realname=ars.get("realname"),
            password = ars.get("password"),
            email=ars.get("email")
        )
        print ars
        self.render("index.html")