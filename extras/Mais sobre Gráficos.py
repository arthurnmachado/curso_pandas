#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15,8))


# In[19]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')
dados.head()


# In[20]:


area = plt.figure() 


# In[21]:


g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)


# In[22]:


g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor X Área')


# In[23]:


area


# In[24]:


g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor X Área')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100) 
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra (Valor)')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')


# In[25]:


area


# In[26]:


area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')


# In[ ]:




