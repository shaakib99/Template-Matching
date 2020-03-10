#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


def gray_transform(img):
    r,c,ch = img.shape
    new_img = np.zeros([r,c])
    for i in range(r):
        for j in range(c):
            new_img[i,j] = 0.33*img[i,j,0] + 0.33*img[i,j,1] + 0.33*img[i,j,2]
    return new_img
