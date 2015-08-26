__author__ = 'xiaobu'
# -*- coding:utf-8 -*-
from tornado import web as web
from apps.showService import ShowService
from apps.tagService import TagService
import os.path

class TagHandler(web.RequestHandler):
    def get(self):
        args = self.request.arguments
        #确保有有pagenum参数，如果没有，设为0，首页
        if "pagenum" in args.keys():
            num = int(args.get("pagenum")[0])
        else:
            num = 1
        show = ShowService()
        data_list,final_tag,num = show.initPicTree(num)

        self.render("tagging.html",table_list=data_list,pagenum=num,final_tag=final_tag,allTagList=show.allTags())


    def post(self):
        args = self.request.arguments
        pagenum = int(args.get("page_num")[0])
        show = ShowService()
        data_list,final_tag,num = show.initPicTree(pagenum)
        print args
        im_path = args.get('image_path')[0].split('pictures/')[1].split('?')[0]
        print im_path

        img_path = os.path.normpath(im_path)
        new_tage_names = args.get('new_tag_names') or []
        tags = args.get('tag') or []

        print img_path
        print new_tage_names
        print tags

        service = TagService()
        for each in new_tage_names:
            service.addTag(each)
        for each in tags:
            service.addTag2Pic(int(each),img_path)



        self.render("tagging.html",table_list=data_list,pagenum=num,final_tag=final_tag,allTagList=show.allTags())

        pass