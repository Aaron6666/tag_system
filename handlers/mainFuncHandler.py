__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

from tornado import web as web


#处理进入系统的请求
class MainFuncHandler(web.RequestHandler):
    def get(self):
        if not self.get_cookie("username"):
            self.set_cookie(name="username",value="abc",expires_days=None)
            #说明：expires_days为设置cookie清空的参数。
            #说明2：如果设为none，意味关闭浏览器立刻清空cookie
            self.render("signin.html")

        else:
            print self.get_cookie("username")
            self.render("upload.html")

    def post(self):
        pass