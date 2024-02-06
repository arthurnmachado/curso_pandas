#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


s = pd.Series(list('asdadeadesdasesda'))
s


# In[3]:


s.unique()


# In[4]:


s.value_counts()


# In[5]:


dados = pd.read_csv("dados/aluguel.csv", sep=";")


# In[6]:


dados.Tipo.unique()


# In[7]:


dados.Tipo.value_counts()


# In[ ]:




