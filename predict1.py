#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
#!/usr/bin/env python
# encoding: utf-8
'''
1、读取指定目录下的所有文件
2、读取文件，正则匹配出需要的内容，获取文件名
3、打开此文件(可以选择打开可以选择复制到别的地方去)
'''
import os.path
import re
from yolo import YOLO
from PIL import Image

yolo = YOLO()

# while True:
#     img = input('Input image filename:')
#     try:
#         image = Image.open(img)
#     except:
#         print('Open Error! Try again!')
#         continue
#     else:
#         r_image = yolo.detect_image(image)
#         r_image.show()
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if os.path.isfile(child):
            readFile(child)
            #print (child.decode('gbk')) # .decode('gbk')是解决中文显示乱码问题
            continue
        eachFile(child)
# 遍历出结果 返回文件的名字
def readFile(filenames):
    fopen = open(filenames, 'r')  # r 代表read
   # fileread = fopen.read()
    image = Image.open(filenames)
    r_image = yolo.detect_image(image)
    r_image.show()
    #fopen.close()
    #t = re.search(r'clearSpitValve', fileread)



if __name__ == "__main__":
    filenames = 'E:\\2QR_T' # refer root dir
    arr=[]
    eachFile(filenames)
    for i in arr:
        print (i)