#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 4

# ## Seleções e frequências

# In[1]:


import pandas as pd


# In[4]:


dados = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados.head()


# In[7]:


#Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]
n1


# In[11]:


#Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao = dados['Tipo'].isin(['Casa', 'Casa de Condomínio', 'Casa de Vila'])
n2 = dados[selecao].shape[0]
n2


# In[12]:


#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
# 60 <= Area <= 100
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
n3


# In[14]:


#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
n4


# In[15]:


print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))


# In[ ]:




