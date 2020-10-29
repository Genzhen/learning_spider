#!/user/bin/env python3
#!-*- coding:utf-8 -*-
'''
Created on 2018年3月27日

@author: RecluseXu
'''

import cv2 as cv
import numpy as np

def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0 , 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    # cv.MORPH有几种，都可以试试。
    # 后面的(3*3)是参数，对应介绍图上面的那个3*3
    dst = cv.erode(binary,kernel) #腐蚀
    cv.imshow('erode',dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0 , 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    # cv.MORPH有几种，都可以试试。
    # 后面的(3*3)是参数，对应介绍图上面的那个3*3
    dst = cv.dilate(binary,kernel) # 膨胀
    cv.imshow('dilate',dst)

src = cv.imread('picture/goodmancard.jpg')
cv.imshow('src',src)

erode_demo(src)
dilate_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()