#!/usr/bin/env python
# coding: utf-8

# # Relatório de Análise 6

# ## Criando Novas Variáveis

# In[33]:


import pandas as pd


# In[34]:


dados = pd.read_csv("dados/aluguel_residencial.csv", sep=";")
dados.head()


# In[35]:


dados["Valor Bruto"] = dados["Valor"] + dados["Condominio"] + dados["IPTU"]


# In[36]:


dados.head()


# In[37]:


dados["Valor m2"] = dados["Valor"] / dados["Area"]
dados.head()


# In[38]:


dados["Valor m2"] = dados["Valor m2"].round(2)
dados.head()


# In[39]:


dados["Valor Bruto m2"] = (dados["Valor Bruto"] / dados["Area"]).round(2)
dados.head()


# In[40]:


casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']


# In[41]:


dados["Tipo Agregado"] = dados.Tipo.apply(lambda x: "Casa" if x in casa else "Apartamento")
dados.head()


# ## Excluindo Variáveis

# In[42]:


dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
dados_aux.head()


# In[43]:


del dados_aux['Valor Bruto']
dados_aux.head()


# In[44]:


dados_aux.pop("Valor Bruto m2")


# In[45]:


dados_aux.head()


# In[46]:


dados.drop(["Valor Bruto", "Valor Bruto m2"], axis=1, inplace=True)
dados.head()


# In[ ]:


dados.to_csv("dados/aluguel_residencial.csv", sep=";", index)

