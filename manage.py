__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

import tornado.ioloop as ioloop
import tornado.web as web
import tornado.httpserver as httpserver
from conf import url_conf,path_conf
import os.path


application = web.Application(
    url_conf.urls,
    template_path=os.path.join(os.path.dirname(__file__),path_conf.TEMPLATE_PATH),
    static_path=os.path.join(os.path.dirname(__file__),path_conf.STATIC_PATH),
)

if __name__=="__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8000)
    ioloop.IOLoop.instance().start()
    print "start"
    #项目主入口