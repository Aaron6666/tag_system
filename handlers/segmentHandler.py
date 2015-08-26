__author__ = 'xiaobu'
# -*- coding:utf-8
from tornado import web as web
from apps.showService import ShowService
import json
from apps.segmentService import SegmentService

class SegmentHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        args = self.request.arguments
        #确保有有pagenum参数，如果没有，设为0，首页
        if "pagenum" in args.keys():
            num = int(args.get("pagenum")[0])
        else:
            num = 1
        show = ShowService()
        data_list,final_tag,num = show.initPicTree(num)

        self.render("segment.html",table_list=data_list,pagenum=num,final_tag=final_tag,allTagList=show.allTags())

    def post(self):
        service = SegmentService()
        args = self.request.arguments
        pagenum = int(args.get("pagenum") and int(args.get("pagenum")[0]) or 1)
        show = ShowService()
        data_list,final_tag = show.initPicTree(pagenum)
        service.cut(self.request.arguments)
        self.render("segment.html",table_list=data_list,pagenum=final_tag and pagenum-1 or pagenum,final_tag=final_tag)