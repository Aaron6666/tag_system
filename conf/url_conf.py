__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

from handlers import *

urls = [
    (r"/",mainHandler.MainHandler),
    (r"/index.html",mainHandler.MainHandler),
    (r"/about.html",aboutHandler.AboutHandler),
    (r"/contact.html",contactHandler.ContactHandler),
    (r'/main_function',mainFuncHandler.MainFuncHandler),
    (r'/upload.html',uploadHandler.UploadHandler),
    (r'/segment.html',segmentHandler.SegmentHandler),
    (r'/tagging.html',tagHandler.TagHandler),
    (r'/manage.html',manageHandler.ManageHandler),
    (r'/signin.html',signinHandler.SigninHandler),
    (r'/signup.html',signupHandler.SignupHandler),

]

#切记！！此处写类名，不是文件名！
