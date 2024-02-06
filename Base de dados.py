#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 1

# ## Importando a base de dados

# In[9]:


import pandas as pd


# In[10]:


# importando
dados = pd.read_csv("dados/aluguel.csv", sep=';')
dados


# In[11]:


type(dados)


# In[12]:


dados.info()


# In[13]:


dados.head(10)


# ## Informações gerais sobre a base de dados

# In[16]:


dados.dtypes


# In[20]:


tipos_de_dados = pd.DataFrame(dados.dtypes, columns=['Tipos de dados'])


# In[21]:


tipos_de_dados.columns.name = 'Variáveis'


# In[22]:


tipos_de_dados


# In[23]:


dados.shape


# In[24]:


dados.shape[0]


# In[25]:


dados.shape[1]


# In[26]:


print("A base de dados apresenta {} registros (imoveis) e {} variaveis".format(dados.shape[0], dados.shape[1]))


# In[ ]:




