#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 7

# ## Criando Agrupamentos

# In[37]:


import pandas as pd


# In[38]:


dados = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados.head()


# https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats

# In[39]:


dados["Valor"].mean()


# In[40]:


bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]


# In[41]:


dados["Bairro"].drop_duplicates()


# In[42]:


grupo_bairro = dados.groupby("Bairro")


# In[43]:


type(grupo_bairro)


# In[44]:


grupo_bairro.groups


# In[45]:


for bairro, data in grupo_bairro:
    print("{} -> {}".format(bairro, data["Valor"].mean()))


# In[46]:


grupo_bairro[["Valor", "Condominio"]].mean().round(2)


# ## Estatísticas Descritivas

# In[47]:


grupo_bairro["Valor"].describe().round(2)


# In[48]:


grupo_bairro["Valor"].aggregate(["min", "max", "sum"]).rename(columns = {'min': 'Minimo', 'max': 'Maximo', 'sum': 'Soma'})


# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))


# In[51]:


fig = grupo_bairro["Valor"].mean().plot.bar(color="blue")
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio de Aluguel por Bairro', {"fontsize": 22})


# In[52]:


fig = grupo_bairro["Valor"].max().plot.bar(color="blue")
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio de Aluguel por Bairro', {"fontsize": 22})


# In[ ]:




