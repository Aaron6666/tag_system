__author__ = 'xiaobu'
#-* coding:utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from conf.db_conf import DBCONFIG

engine = create_engine(
            DBCONFIG[0].get("dbtype")+":///"+DBCONFIG[0].get("name"),
            echo=True
        )
Base = declarative_base()
col = Column


class User(Base):
    __tablename__ = "user"

    id = col(Integer,primary_key=True)
    name = col(String(20),nullable=False,unique=True)
    realname = col(String(20),nullable=False,default='')
    password = col(String(20),nullable=False)
    email = col(String(50),nullable=False,default="[]")



class Pic(Base):

    __tablename__ = 'picture'


    id = col(Integer,primary_key=True)
    name = col(String(20),nullable=True,unique=True)
    path = col(String(100),nullable=True,unique=True)
    parent = col(Integer,nullable=False,default=-1)
    children = col(String(100),nullable=False,default='[]')
    tag_list = col(String(100),nullable=True,default='[]')
    description= col(String(200),nullable=True,default='')




class Tag(Base):
    __tablename__ = 'tag'

    id = col(Integer,primary_key=True)
    name = col(String(20),nullable=False,unique=True)
    description = col(String(200),nullable=True,default='')


Base.metadata.create_all(engine)

#表设计还处于初步，没有复杂的计算

#User和pic是否有从属关系

#Pic和Tag肯定有主外键的关系，但是需要怎么维护和设置？

