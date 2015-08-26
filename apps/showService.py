__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

from dbService import DBService
from model import Pic,Tag
import os.path


class ShowService(object):
    def __init__(self):
        pass


    #获取全部根图
    #返回为全部根节点的id列表
    def getRootPics(self):
        db = DBService(Pic,Pic.__tablename__)
        root_list = []
        for each in  db.searchAll(Pic.parent==-1):
            root_list.append(each.id)
        return root_list

    #根据跟列表和传入的页码生成展示树的数据表
    def initPicTree(self,page_num):
        final_tag=0
        db = DBService(Pic,Pic.__tablename__)
        root_list = self.getRootPics()
        #总长度
        allpage_num = len(root_list)
        num = 0
        if page_num< 1:
            num =0
        elif page_num < allpage_num:
            num = page_num-1
        else:
            num = allpage_num-1
            final_tag = 1

        tree_id_list = [root_list[num]]
        data_list =  []
        while tree_id_list:
            pic = tree_id_list[0]
            tree_id_list=tree_id_list[1:]
            data = db.searchRecord(Pic.id==pic)
            tags = eval(data.tag_list)
            tagnames = []
            tgService = DBService(Tag,Tag.__tablename__)
            for each in tags:
                tagnames.append(tgService.searchRecord(Tag.id==each).name)
            parent_name = ''
            if not data.parent==-1:
                parent_name = db.searchRecord(Pic.id==data.parent).name
            data_list.append({'name':data.name,'path':("pictures\\"+data.path).replace('\\','\\\\'),'parent_name':parent_name,'description':data.description,'taglist':tagnames})
            tree_id_list+=eval(data.children)
        return data_list,final_tag,num+1


    def allTags(self):
        db = DBService(Tag,Tag.__tablename__)
        model_list = db.searchAll(Tag.id!=-1)
        return [(item.name,item.id) for item in model_list]

