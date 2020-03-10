#!/usr/bin/env python
# coding: utf-8

# In[91]:


import matplotlib.pyplot as plt
from rgb2gray import *


# In[92]:


def otsu_rgb2bin(img):
    gray_img = gray_transform(img)
    gray_img =gray_img.astype('uint8')
#     plt.imshow(gray_img,cmap="Greys_r")
    r,c = gray_img.shape
    within_class_varience_holder = []
    
    '''
        Finding Number of Every Intensity Pixel
        0 -> 36 times
        .
        .
        .
        255 ->4 times
    ''' 
    
    pixel_intensity_holder = np.zeros([256]).astype('uint8')
    
    for i in range(r):
        for j in range(c):
            pixel_intensity_holder[gray_img[i,j]] += 1
#     print(pixel_intensity_holder)
            
    '''
        BACKGROUNG & FORGROUND
    '''
    intensities = 256 # For Gray Image intensity = 256, 0-255
    for intensity in range(intensities):
        
        background_pixel = intensity
        forground_pixel = 256- intensity
        total_pixel = r*c

        '''
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        '''
        # For Background Pixel Counting weight, mean, and varience
        # Weight & Mean for background Pixel
        wb = 0
        mb = 0 
        pixel_counter_b = 0
        for i in range(background_pixel):
            
            pixel_counter_b += pixel_intensity_holder[i]
            
            wb += pixel_intensity_holder[i]
            mb += i * pixel_intensity_holder[i]
        wb = wb / total_pixel
        try:
            mb = mb / pixel_counter_b
        except:
            mb = 0
        
        # Varience for background Pixel
        vb = 0
        for i in range(background_pixel):
            vb += ((i-mb)**2)*pixel_intensity_holder[i]
        try:
            vb = vb / pixel_counter_b
        except:
            vb = 0
            
        # For Forground Pixel Counting weight, mean, and varience
        ww = 0
        mw = 0 
        pixel_counter_w = 0
        for i in range(forground_pixel):
            
            pixel_counter_w += pixel_intensity_holder[i]
            
            ww += pixel_intensity_holder[i]
            mw += i * pixel_intensity_holder[i]
        ww = ww / total_pixel
        try:
            mw = mw / pixel_counter_w
        except:
            mw = 0
        
        # Varience for background Pixel
        vw = 0
        for i in range(forground_pixel):
            vw += ((i-mw)**2)*pixel_intensity_holder[i]
        try:
            vw = vw / pixel_counter_b
        except:
            vw = 0
        '''
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        '''
        
        # Counting Within Class Varience & Keeping it in a array
        
        within_class_varience = wb * vb + ww * vw
        
        # Saving it in a array
        within_class_varience_holder.append(within_class_varience)
    
    
    # Finding Threshold from within_class_varience_holder
    threshold = within_class_varience_holder.index(min(within_class_varience_holder))
    # Converting to binary image using Threshold Value
    bin_img = np.zeros([r,c])
    for i in range(r):
        for j in range(c):
            if gray_img[i,j] > threshold:
                bin_img[i,j] = 1
            else:
                bin_img[i,j] = 0
    
    
    return bin_img

