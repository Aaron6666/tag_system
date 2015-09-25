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
        """

        :param name: 需要检查的名字
        :param psw: 输入的密码
        :return:检查结果
        code:-1为无用户，0为密码错误，1为正确返回
        """
        code = 1
        service = DBService(User,User.__tablename__)
        result = service.searchRecord(User.name==name)
        if result:
            if result.password == psw:
                return code,True
            else:
                return code-1,False
        else:
            code=-1
            return code,None

