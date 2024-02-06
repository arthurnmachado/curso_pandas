#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 5

# ## Tratamento de Dados Faltantes

# In[2]:


import pandas as pd


# In[4]:


dados = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados.head()


# In[5]:


dados.isnull()


# In[6]:


dados.notnull()


# In[7]:


dados.info()


# In[8]:


dados[dados['Valor'].isnull()]


# In[9]:


A = dados.shape[0]
A


# In[11]:


dados.dropna(subset=['Valor'], inplace=True)
dados.shape[0]


# In[12]:


A - dados.shape[0]


# In[13]:


dados[dados['Valor'].isnull()]


# ## Tratamento de Dados Faltantes (continuação)

# In[14]:


dados[dados['Condominio'].isnull()].shape[0]


# In[15]:


selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())


# In[16]:


A = dados.shape[0]
A


# In[19]:


dados = dados[~selecao]
dados.shape[0]


# In[20]:


A - dados.shape[0]


# In[21]:


dados[dados['Condominio'].isnull()].shape[0]


# In[22]:


dados.fillna(0, inplace=True)


# In[27]:


dados[dados['Condominio'].isnull()].shape[0]


# In[28]:


dados[dados['IPTU'].isnull()].shape[0]


# In[29]:


dados.info()


# In[30]:


dados.to_csv("dados/aluguel_residencial.csv", sep=";", index=False)

