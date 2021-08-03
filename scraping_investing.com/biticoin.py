#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
import requests

from time import sleep
# parsing do HTML
from bs4 import BeautifulSoup

# expressões regulares
import re


# In[2]:


driver = Chrome()


# In[31]:


driver = Chrome()


url = 'https://br.investing.com/crypto/bitcoin/bitcoin-futures-historical-data'
# driver = webdriver.Chrome(r"C:\Users\Desktop\Documents\PUC\Aplicativos\chromedriver\chromedriver.exe")
driver.get(url)
sleep(3)

# titulo_text = driver.find_elements_by_class_name('title-holder')
# localizacao_text = driver.find_elements_by_class_name('hidden-xs ng-binding')


# In[1]:


table_textd = driver.find_elements_by_class_name('genTbl.closedTbl.historicalTbl')


# In[238]:


table_textd


# In[239]:


statusdo = ''
for s in table_textd:
    a = s.text
    a = re.sub(r' ', '\t', a)
    a = re.sub(r'(\t(18))', '18', a)
    a = re.sub(r'(\t(20))', '20', a)
    a = re.sub(r'(\t(19))', '19', a)
    a = re.sub(r'(\t(21))', '21', a)
    statusdo += a + '\n'
statusdo


# In[240]:


print(statusdo)


# In[241]:


arquivo = open("dolar_table.csv", "w", encoding='utf-8')
arquivo.write(statusdo)
arquivo.close()


# In[326]:


t = pd.read_csv('do_table.csv', sep = '\t')


# In[327]:


display(t)


# In[293]:


fechamentobra = []
for f in t['Último']:
    fe = re.sub('\.', '', f)
    fe = re.sub(',', '.', fe)
    fe = 1/float(fe)
    fechamentobra.append(float(fe))
fechamentobra


# In[328]:


fechamentod = []
for f in t['Último']:
    fe = re.sub('\.', '', f)
    fe = re.sub(',', '.', fe)
    fe = 1/float(fe)
    fechamentod.append(float(fe))
fechamentod


# In[370]:


fechamentob = []
for f in fechamento:
    fe = f/1
    fechamentob.append(fe)
fechamentob


# In[36]:


import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)


# In[374]:


trace_do = go.Scatter(x = data,
                    y = fechamentod,
                    mode = 'lines',
                    name = 'Dólar')


layout = go.Layout(title = "Variação da cotação de algumas moedas em relação ao Euro a cada mês(2018-2021)",
                   xaxis_title = 'Mês',
                   yaxis_title = 'Valor de fechamento')

trace_bra = go.Scatter(x = data,
                    y = fechamentobra,
                    mode = 'lines',
                    name = 'Real')

data = [trace_bra,trace_btc, trace_do]

fig = go.Figure(data = data, layout = layout)
py.iplot(fig)


# In[373]:


t = t.loc[0:,['Data', 'Último']]
data = []

for d in t['Data']:
    data.append(d)
data


# In[372]:


trace_btc = go.Scatter(x = data,
                    y = fechamentob,
                    mode = 'lines',
                    name = 'Biticon')

data = [trace_btc]
layout = go.Layout(title = "Variação da cotação de algumas moedas em relação ao Euro a cada mês(2018-2021)",
                   xaxis_title = 'Mês',
                   yaxis_title = 'Valor de fechamento')
fig = go.Figure(data = data, layout = layout)
py.iplot(fig)

