#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 8

# ## Identificando e Removendo Outliers

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[2]:


dados = pd.read_csv("dados/aluguel_residencial.csv", sep=";")


# In[3]:


dados.boxplot(["Valor"])


# In[4]:


dados[dados["Valor"] >= 500000]


# In[5]:


valor = dados["Valor"]


# In[6]:


Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


# In[9]:


selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]


# In[11]:


dados_new.boxplot(['Valor'])


# In[10]:


dados.hist(['Valor'])
dados_new.hist(['Valor'])


# ## Identificando e Removendo Outliers (Continuação)

# In[12]:


dados.boxplot(['Valor'], by = ['Tipo'])


# In[15]:


grupo_tipo = dados.groupby('Tipo')['Valor']


# In[16]:


type(grupo_tipo)


# In[17]:


grupo_tipo.groups


# In[18]:


Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


# In[19]:


limite_superior['Apartamento']


# In[20]:


for tipo in grupo_tipo.groups.keys():
    print(tipo)


# In[21]:


for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados[selecao]


# In[22]:


dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])


# In[23]:


dados_new.boxplot(['Valor'], by = ['Tipo'])


# In[24]:


dados_new.to_csv('dados/aluguel_residencial_sem_outliers.csv', sep = ';', index = False)


# In[ ]:




