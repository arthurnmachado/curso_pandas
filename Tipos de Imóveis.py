#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 2

# ## Tipos de Imóveis

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv("dados/aluguel.csv", sep=";")


# In[3]:


dados.head()


# In[4]:


dados["Tipo"]


# In[5]:


dados.Tipo


# In[6]:


tipo_de_imovel = dados['Tipo']
type(tipo_de_imovel)


# In[7]:


tipo_de_imovel.drop_duplicates()


# In[8]:


tipo_de_imovel


# In[9]:


tipo_de_imovel.drop_duplicates(inplace=True)


# In[10]:


tipo_de_imovel


# ## Organizando a Visualização

# In[11]:


tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
tipo_de_imovel


# In[12]:


tipo_de_imovel.index


# In[15]:


tipo_de_imovel.shape[0]


# In[16]:


tipo_de_imovel.index = range(tipo_de_imovel.shape[0])


# In[17]:


tipo_de_imovel


# In[18]:


tipo_de_imovel.columns.name = 'Id'


# In[19]:


tipo_de_imovel


# In[ ]:




