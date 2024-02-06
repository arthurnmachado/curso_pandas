#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]
data


# In[5]:


index = list('321')
index


# In[6]:


columns = list('ZYX')
columns


# In[7]:


df = pd.DataFrame(data=data, index=index, columns=columns)
df


# In[8]:


df.sort_index(inplace = True)
df


# In[9]:


df.sort_index(inplace = True, axis=1)
df


# In[10]:


df.sort_values(by = "X", inplace=True)
df


# In[11]:


df.sort_values(by = "3", axis=1, inplace=True)
df


# In[12]:


df.sort_values(by = ['X', 'Y'], inplace=True)
df


# In[ ]:




