__author__ = 'xiaobu'


# -*- coding:utf-8 -*-

import os,os.path

CORRENT_PATH = os.path.dirname(__file__)
MAIN_PATH = os.path.dirname(CORRENT_PATH)
STATIC_PATH = os.path.join(MAIN_PATH,"static")
PIC_PATH = os.path.join(STATIC_PATH,"pictures")
TEMPLATE_PATH = os.path.join(MAIN_PATH,"templates")
CACHE_PATH = os.path.join(STATIC_PATH,"cache")