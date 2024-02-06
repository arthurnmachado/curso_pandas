#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Series

# In[2]:


data = [1, 2, 3, 4, 5]


# In[6]:


s = pd.Series(data)
s


# In[5]:


index = ["Linha" + str(i) for i in range(5)]
index


# In[7]:


s = pd.Series(data=data, index=index)
s


# In[9]:


data = {"Linha" + str(i): i + 1 for i in range(5)}
data


# In[10]:


s = pd.Series(data)
s


# In[11]:


s1 = s + 2
s1


# In[12]:


s2 = s + s1
s2


# # DataFrame

# In[13]:


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]
data


# In[14]:


df1 = pd.DataFrame(data)
df1


# In[15]:


index = ["Linha" + str(i) for i in range(3)]
index


# In[17]:


df1 = pd.DataFrame(data=data, index=index)
df1


# In[19]:


columns = ["Coluna" + str(i) for i in range(3)]
columns


# In[20]:


df1 = pd.DataFrame(data=data, index=index, columns=columns)
df1


# In[21]:


data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
        'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
        'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
data


# In[22]:


df2 = pd.DataFrame(data)
df2


# In[23]:


data = [(1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9)]
data


# In[24]:


df3 = pd.DataFrame(data=data, index=index, columns=columns)
df3


# In[25]:


df1[df1 > 0] = 'A'
df1


# In[26]:


df2[df2 > 0] = 'B'
df2


# In[27]:


df3[df3 > 0] = 'C'
df3


# In[28]:


df4 = pd.concat([df1, df2, df3])
df4


# In[29]:


df4 = pd.concat([df1, df2, df3], axis=1)
df4


# In[ ]:




