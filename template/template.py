#!/usr/bin/env python
# coding: utf-8

# In[6]:


import otsu_bin as otsu
import math
import cv2 as cv
import matplotlib.pyplot as plt


# In[2]:


def find_square_sum(img):
    r,c = img.shape
    s = 0
    for i in range(r):
        for j in range(c):
            s += img[i,j]**2
    return s


# In[3]:


def conv(img,temp):
    img_r,img_c = img.shape
    temp_r,temp_c = temp.shape
    s = 0
    for i in range(img_r):
        for j in range(img_c):
            s += img[i,j] * temp[i,j]
    return s


# In[4]:


# def normalissed_cross_correlation(template,candidate):
#     y = find_square_sum(template)
#     b = find_square_sum(candidate)
#     x = conv(candidate,template) / (math.sqrt(b * y))
#     return x
#     #return (conv(candidate,template) / (math.sqrt(find_square_sum(candidate) * find_square_sum(template))))


# In[2]:


def find_template(threshold,template,candidate_list):
    z = template
    for each_candidate in candidate_list:
        candidate = each_candidate
        template_bin = otsu.otsu_rgb2bin(template)
        candidate_bin = otsu.otsu_rgb2bin(candidate)
        t_r,t_c = template_bin.shape
        c_r,c_c = candidate_bin.shape

        row = 0
        col = 0
        i = 0

        if t_r > c_r or t_c > c_c:
            while(row<= (t_r - c_r)):
                col = 0
                while(col<= (t_c - c_c)):
                    start_row = row
                    end_row = row + c_r

                    start_col = col
                    end_col = col + c_c

                    currnt_matrix = template_bin[start_row:end_row,start_col:end_col]
                    conv1 = conv(currnt_matrix,candidate_bin)
                    candidate_square = find_square_sum(candidate_bin)
                    currnt_square = find_square_sum(currnt_matrix)
                    m = conv1 / math.sqrt(candidate_square * currnt_square)
        #             print(start_row,start_col,end_row,end_col,m)
                    if m > threshold:
                        print(start_row,start_col,end_row,end_col,m)
                        z = cv.rectangle(template,(start_col,start_row),(end_col,end_row),(0, 255, 0),2)
                    col += 1
                row += 1
        else:
            print("Candidate Size is Bigger than Template")
    plt.imshow(z)
    plt.waitforbuttonpress(0)

