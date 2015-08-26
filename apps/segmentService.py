__author__ = 'xiaobu'
#-*- coding:utf-8 -*-
import cv2
import numpy as np
import scipy
from PIL import Image as im
from conf.path_conf import CACHE_PATH,PIC_PATH
import os,os.path


class SegmentService(object):
    def __init__(self):
        pass

    def cut(self,args):
        path = os.path.normpath(args.get('image')[0].split('pictures/')[1].split('?')[0])
        x = int(args.get('x')[0])
        y = int(args.get('y')[0])
        w = int(args.get('w')[0])
        h = int(args.get('h')[0])
        bg_list = []
        fg_list = []
        for index in range(len(args.get('x_list_fg[]'))):
            fg_list.append((int(args.get('x_list_fg[]')[index]),int(args.get('y_list_fg[]')[index])))
        for index in range(len(args.get('x_list_bg[]'))):
            bg_list.append((int(args.get('x_list_bg[]')[index]),int(args.get('y_list_bg[]')[index])))

        self.test_seg_alert((x,y,w,h),fg_list,bg_list,path)


        pass


    def convert(self,img_path):#处理图，规整图片的格式
        pic_path = os.path.normpath(PIC_PATH)
        path =pic_path+img_path
        image = im.open(path,'r')
        if image.mode == 'L':
            img_temp = image.convert('RGB')
        if image.mode == 'RGBA':
            image = im.open(img_path)
            img_temp = im.new('RGB',image.size,(255,255,255))
            x,y = image.size
            img_temp.paste(image,(0,0,x,y),image)
        else:
            img_temp = image
        img_temp.save(os.path.join(CACHE_PATH,"temp.jpg"))
        return True

    def test_seg_alert(self,rect,points_fg,points_bg,img_path):
        self.convert(img_path)

        image = 255-cv2.imread('temp.jpg')
        print image.shape
        print 1
        mask = np.zeros(image.shape[:2],np.uint8)
        print 2
        for each in points_fg:
            cv2.circle(mask,(each[0],each[1]),4,1,-1)
        for each in points_bg:
            cv2.circle(mask,(each[0],each[1]),4,0,-1)
        print 3



        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)

        print 4
        cv2.grabCut(image,mask,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_MASK)
        #mask2 = np.where((mask==1)|(mask==3),255,0).astype('uint8')
        #output = cv2.bitwise_and(image,image,mask=mask2)
        print 5

        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        image = image*mask2[:,:,np.newaxis]




        # for each in points_fg:
        #     image[each[1]][each[0]]=255
        # for each in points_bg:
        #     image[each[1]][each[0]]=0

        cv2.imwrite(os.path.join(CACHE_PATH,'temp2.jpg'),255-image)
        print 'a'
        im_old = im.open(os.path.join(CACHE_PATH,'temp2.jpg'))
        print rect[0],rect[1],rect[0]+rect[2],rect[1]+rect[3]
        im_new = im_old.crop((rect[0],rect[1],rect[0]+rect[2],rect[1]+rect[3]))



        try:
            os.mkdir(os.path.splitext(img_path)[0])
        except:
            new_path = os.path.splitext(img_path)[0]
        finally:
            new_path = os.path.splitext(img_path)[0]
        file_num = 0
        for each_file in os.listdir(new_path):
            if each_file.split(".")[1]:
                file_num += 1
