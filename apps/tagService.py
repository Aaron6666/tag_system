__author__ = 'xiaobu'
# -*- coding:utf-8 -*-
from model import Tag
from apps.dbService import DBService

class TagService(object):
    def __init__(self):
        self.db = DBService(Tag,Tag.__tablename__)
        pass

    def addTag(self,tag_name):
        self.db.addRecord(Tag(name=tag_name))
        pass

    def addTag2Pic(self,tag_id,pic_path):
        pass

    #查看标签是否存在
    def tagExist(self,tagname):
        if self.db.searchRecord(Tag.name==tagname):
            return self.db.searchRecord(Tag.name==tagname).id
        return 0