__author__ = 'xiaobu'
# -*- coding:utf-8 -*-

import model
from sqlalchemy import create_engine,Table

from sqlalchemy.orm import sessionmaker
from conf.db_conf import DBCONFIG


class DBService(object):

    def __init__(self,type,table_name):
        self.table_name = table_name
        self.type = type
        self.engine = model.engine

    def create_session(self):
        DBsession = sessionmaker(bind=self.engine)
        return DBsession()

    def close_session(self,session):
        session.close()
        pass



    def addRecord(self,record):
        session = self.create_session()
        session.add(record)
        session.commit()
        self.close_session(session)
    #ok



    def deleteRecord(self,condition):
        session = self.create_session()
        session.query(self.type).filter(condition).delete()
        session.commit()
        self.close_session(session)
        pass

    #new
    def updateRecord(self,condition,item,new_value):
        session = self.create_session()
        session.query(self.type).filter(condition).update({item:new_value})
        session.commit()
        session.close()

    #参数condition格式为model.User.name=='zhangsan'
    #返回的是对象格式的结果，可以从中截取想要的信息
    #需要重新修改，将函数改成适合多种类型的
    def searchRecord(self,condition):
        session=self.create_session()
        result = session.query(self.type).filter(condition).first()
        session.close()
        return result

    def searchAll(self,condition):
        session=self.create_session()
        result = session.query(self.type).filter(condition).all()
        self.close_session(session)
        return result



if __name__=="__main__":
    dbserer = DBService(model.Pic,model.Pic.__tablename__)
    #使用示例
    #dbserer.addRecord(model.User(name=u"zhangsan",password=u"123456"))
    #dbserer.addRecord(model.Pic(name=u"abccddd",path=u"1cc23"))
    #dbserer.addRecord(model.Tag(name=u"祥云"))
    #dbserer.deleteRecord(model.User.name=='zhangsan')
    print dbserer.updateRecord(model.Pic.parent==-1,model.Pic.children,'[1,2]')


    print "***"
    #print dbserer.searchRecord(model.Pic.parent==-1)
    print "***"
    # for each in dbserer.searchRecord(model.Tag):
    #     print each.name
