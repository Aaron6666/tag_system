__author__ = 'xiaobu'
# -*- coding:utf-8 -*-
from model import User
from dbService import DBService
class SignupService(object):
    def __init__(self):
        pass

    # def f(a,*b,**c):的用法
    # 第一个参数至a
    # 余下的全部至b，元组形式
    # 以x=y形式标注的，至c，然后用字典方式取出

    def signup(self,**kwargs):
        user= User(
            name=str(kwargs.get("username")),
            realname=str(kwargs.get("realname")),
            password = str(kwargs.get("password")),
            email=str(kwargs.get("email"))
        )
        db = DBService(User,User.__tablename__)
        db.addRecord(user)
        pass