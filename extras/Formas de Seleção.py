#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


'l1 l2 l3 l4'.split() 


# In[4]:


data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df


# In[5]:


df['c1']


# In[7]:


df[['c1', 'c3']]


# In[8]:


type(df[['c1', 'c3']])


# In[9]:


df[:]


# In[10]:


df[1:]


# In[12]:


df[1:3]


# In[13]:


df[1:][['c1', 'c3']]


# In[15]:


df


# In[14]:


df.loc['l3']


# In[16]:


df.loc[['l3', 'l2']]


# In[17]:


df.loc['l1', 'c2']


# In[18]:


df.iloc[0, 1]


# In[19]:


df.loc[['l3', 'l1'], ['c4', 'c1']]


# In[20]:


df.iloc[[2, 0], [3, 0]]


# In[ ]:




