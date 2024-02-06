#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
s


# In[3]:


s.fillna(0)


# In[4]:


s.fillna(method='ffill')


# In[5]:


s.fillna(method='bfill')


# In[6]:


s.fillna(s.mean())


# In[7]:


s


# In[9]:


s1 = s.fillna(method='ffill', limit=1)
s1


# In[10]:


s1.fillna(method='bfill', limit=1)


# In[ ]:




