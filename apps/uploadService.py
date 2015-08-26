__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

import zipfile
from conf.path_conf import PIC_PATH,CACHE_PATH
import os.path,os
from dbService import DBService
from model import Pic


class UploadService(object):
    def __init__(self):
        pass

    def savePic(self,data):
        _result = 1,"ok"
        try:
            file_name =data.get('filename')
            filename,realpath = self.makedir(file_name)
            with open(os.path.join(realpath,file_name),"wb") as fp:
                fp.write(data.get('body'))
            db = DBService(Pic,Pic.__tablename__)
            db.addRecord(Pic(name=file_name,path=os.path.join('\\',filename, file_name).replace('\\','\\\\')))
        except Exception as e:
            _result = -1,"Error\nexception message :"+e.message
        finally:
            return _result



    def makedir(self,filename):
        name = os.path.splitext(filename)[0]
        if not os.path.exists(os.path.join(PIC_PATH,name)):
            os.mkdir(os.path.join(PIC_PATH,name))
        return name,os.path.join(PIC_PATH,name)


    def isZipFIle(self,filename):
        filetype = os.path.splitext(filename)[1]
        if filetype == '.zip':
            return True
        return False


    def isPIcFile(self,filename):

        return False

    def saveZipFile(self,data):
        try:
            db = DBService(Pic,Pic.__tablename__)
            file_name =data.get('filename')
            name,path =self.makedir("zip-"+file_name)
            #存入CACHE_PATH文件夹中
            with open(os.path.join(CACHE_PATH,file_name),"wb") as fp:
                fp.write(data.get('body'))
            zipfileData = zipfile.ZipFile(os.path.join(CACHE_PATH,file_name))
            files = []
            for each in zipfileData.filelist:
                name = str(zipfileData.extract(each,path))
                if os.path.splitext(name)[1]:
                    files.append(name.split(str(os.path.normpath(PIC_PATH)))[1])
            for each_file in files:
                db.addRecord(Pic(name=each_file.replace('\\','-') ,path=each_file))
            for each_file_a in files:
                children_list = []
                parent_id = db.searchRecord(Pic.path==each_file_a).id
                for each_file_b in files:
                    if os.path.split(each_file_b)[0]==os.path.splitext(each_file_a)[0]:
                        children_list.append(db.searchRecord(Pic.path==each_file_b).id)
                        db.updateRecord(Pic.path==each_file_b,Pic.parent,parent_id)
                db.updateRecord(Pic.path==each_file_a,Pic.children,str(children_list))


        except Exception as e:
            _result = -1,"Error\nexception message :"+e.message






    #聚合文件存储接口，提供统一服务
    def save(self,filedata):
        file_name =filedata.get('filename')
        if os.path.splitext(file_name)[1]=='.zip':
            self.saveZipFile(filedata)
        else:
            self.savePic(filedata)
