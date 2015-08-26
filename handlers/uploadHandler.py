__author__ = 'xiaobu'



from  tornado import web as web
from apps.dbService import DBService
from apps.uploadService import UploadService
from model import *
import os.path
from conf.path_conf import PIC_PATH
from apps.showService import ShowService

class UploadHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upload.html")

    def post(self, *args, **kwargs):
        arg = self.request.arguments
        files = self.request.files['file_data']
        for eachfile in files:
            uploadService = UploadService()
            uploadService.save(eachfile)