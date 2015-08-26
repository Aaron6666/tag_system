__author__ = 'xiaobu'
# -*- coding:utf-8 -*-
from model import Tag,Pic
from apps.dbService import DBService
import os.path

class TagService(object):
    def __init__(self):
        self.tag_db = DBService(Tag,Tag.__tablename__)
        self.pic_db = DBService(Pic,Pic.__tablename__)
        pass

    def addTag(self,tag_name):
        self.tag_db.addRecord(Tag(name=tag_name))

    def addTag2Pic(self,tag_id,pic_path):
        result = self.pic_db.searchRecord(Pic.path==pic_path) \
                 or self.pic_db.searchRecord(Pic.name==os.path.split(pic_path)[1])
        tag_list = result.tag_list
        print tag_id
        tags = eval(tag_list)
        tags.append(tag_id)
        print os.path.split(pic_path)[1]
        try:
            self.pic_db.updateRecord(Pic.path==pic_path,Pic.tag_list,str(tags))
        except:
            self.pic_db.updateRecord(Pic.name==os.path.split(pic_path)[1],Pic.tag_list,str(tags))
        pass

    #查看标签是否存在
    def tagExist(self,tagname):
        if self.db.searchRecord(Tag.name==tagname):
            return self.db.searchRecord(Tag.name==tagname).id
        return 0