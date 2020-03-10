#!/usr/bin/env python
# coding: utf-8

# # Importing Necessary Library FIle

# In[1]:


import matplotlib.pyplot as plt
import template


# # Reading Candidate Image & Template Image

# In[2]:


template1 = plt.imread('two.jpeg')
candidate1 = plt.imread('two2.jpg')
candidate2 = plt.imread('two4.jpg')


# # ADDING MULTIPLE CANDIDATE IN A LIST

# In[3]:


candidate_list = [candidate1,candidate2]


# # THRESHOLDING

# In[4]:


threshold = 0.91 # Above 95% Accuracy


# # Template Matching

# In[5]:


template.find_template(threshold,template1,candidate_list)

