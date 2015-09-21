__author__ = 'zar'
# -*- coding:utf-8 -*-
from dbService import DBService
from model import Pic
import hashlib

class CheckFileService(object):
    """
    提供文件校验过程，上传时先经过此类提供的方法进行校验，然后决定是否入库
    1. 获取当前MD5
    2. 查询库中是否有此MD5
    3. 返回结果
    """
    @staticmethod
    def __getMD5(self,file):
        #获取文件的MD5码数

        pass
    @staticmethod
    def exist(self,file):
        #判断库中是否由此文件
        flag = False


        return flag

