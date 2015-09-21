__author__ = 'xiaobu'
#-*- coding:utf-8 -*-
from dbService import DBService
from model import User

class SigninService(object):
    def __init__(self):
        pass

    #检查用户是否在数据库中
    #目前只匹配用户记录是否在库中，不做提示
    def CheckOutUser(self,name,psw):
        service = DBService(User.__tablename__,User)
        if service.searchRecord(User.name==name).password ==psw:
            return True
        return False
