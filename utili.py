# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:35:57 2020

@author: User
"""
import cv2




def video_preprocessing(fg):
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    
    #Opening is just another name of erosion followed by dilation. 
    fgmask = cv2.morphologyEx(fg, cv2.MORPH_OPEN, kernel, iterations =2)
    
    # cv2.imshow('opening',fgmask)
    
    #It is useful in closing small holes inside the foreground objects, or small black points on the object.
    closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations =5)
    
    # cv2.imshow('closing',closing)
    
    return closing

def finding_contours(closing,width,height,frame):
    
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rect=[]

    # cv2.drawContours(frame, contours,-1,(0,255,0),5)
    
    # cv2.imshow('Drawing contours',frame)
    
    MIN_CONTOUR_WIDTH=width
    MIN_CONTOUR_HEIGHT=height
        
        
    for contour in contours:
            
        x,y,w,h = cv2.boundingRect(contour)
            
        if w >= MIN_CONTOUR_WIDTH and h >= MIN_CONTOUR_HEIGHT:
        
            rect.append( [x,y,w,h])
    
    return rect

def create_rect(rect,frame):
    line_color = (0, 255, 0)
    

    for (x, y, w, h) in rect:
        
        top_left = (x, y)
        bottom_right = (x + w, y + h)

        cv2.rectangle(frame, top_left, bottom_right, color=line_color, thickness=2)
    
    return

def find_centroid(rect):
    
    centroid_list=[]
    
    for rect_1 in rect:
        for x,y,w,h in rect_1:
            x1 = int(w / 2)
            y1 = int(h / 2)
            cx = x + x1
            cy = y + y1
        
            centroid_list.append((cx,cy))
        
    return centroid_list    

