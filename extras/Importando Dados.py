#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


json = open('dados/aluguel.json')
print(json.read())


# In[4]:


df_json = pd.read_json('dados/aluguel.json')
df_json


# In[5]:


txt = open('dados/aluguel.txt')
print(txt.read())


# In[6]:


df_txt = pd.read_table('dados/aluguel.txt')
df_txt


# In[7]:


df_xlsx = pd.read_excel('dados/aluguel.xlsx')
df_xlsx


# In[9]:


df_html = pd.read_html("dados/dados_html_1.html") # tambem funciona com a url do site
df_html[0]


# In[10]:


df_html = pd.read_html("dados/dados_html_2.html")


# In[11]:


len(df_html)


# In[12]:


df_html[0]


# In[13]:


df_html[1]


# In[14]:


df_html[2]


# In[ ]:




