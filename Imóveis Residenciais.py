#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 3

# ## Imóveis Residenciais

# In[1]:


import pandas as pd


# In[2]:


dados = pd.read_csv("dados/aluguel.csv", sep=";")


# In[3]:


dados.head()


# In[4]:


list(dados["Tipo"].drop_duplicates())


# In[5]:


residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']
residencial


# In[6]:


dados.head(10)


# In[9]:


selecao = dados["Tipo"].isin(residencial)
selecao


# In[10]:


dados_residencial = dados[selecao]
dados_residencial


# In[11]:


list(dados_residencial["Tipo"].drop_duplicates())


# In[13]:


dados_residencial.shape[0]


# In[14]:


dados.shape[0]


# In[17]:


dados_residencial.index = range(dados_residencial.shape[0])
dados_residencial


# ## Exportando a Base de Dados

# In[18]:


dados_residencial.to_csv("dados/aluguel_residencial.csv", sep=";")


# In[19]:


dados_residencial_2 = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados_residencial_2


# In[20]:


dados_residencial.to_csv("dados/aluguel_residencial.csv", sep=";", index=False)


# In[21]:


dados_residencial_2 = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados_residencial_2


# In[ ]:




