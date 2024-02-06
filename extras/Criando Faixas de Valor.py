#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head(10)


# In[3]:


# 1 e 2
# 3 e 4
# 5 e 6
# 7 e 8
classes = [0, 2, 4, 6, 100]


# In[4]:


quartos = pd.cut(dados["Quartos"], classes)
quartos


# In[5]:


pd.value_counts(quartos)


# In[6]:


labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']


# In[8]:


quartos = pd.cut(dados["Quartos"], classes, labels=labels)
quartos


# In[9]:


pd.value_counts(quartos)


# In[10]:


quartos = pd.cut(dados["Quartos"], classes, labels=labels, include_lowest=True)


# In[11]:


pd.value_counts(quartos)


# In[ ]:




