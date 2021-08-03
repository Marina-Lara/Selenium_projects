#!/usr/bin/env python
# coding: utf-8

# In[2]:

#importando bibliotecas
from selenium import webdriver
from time import sleep
import csv
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import re
from time import sleep


# In[5]:


#configurações do driver
driver = Chrome()

driver.get('https://www.instagram.com/')
sleep(5)


# In[6]:


#lista que irá armazenar as datas com posts com localização no restaurante coco bambu 
date_co = []


# In[33]:


for i in range(0,1000):
    sleep(3)
    postdate_co = driver.find_element_by_xpath('.//time').get_attribute('title') #encontando data na publicação
    date_co.append(postdate_co) #armazenando na lista
    print(i) #monitorando número de publcações já analizadas 
    click = driver.find_element_by_link_text('Próximo').click() #clicando no botão para ir para o próximo post


# In[34]:


print(date_co) #verificando


# In[173]:


date = []
for i in date_co:
    i = re.sub('janeiro de ', '01-', i)
    i = re.sub('fevereiro de ', '02-', i)
    i = re.sub('março de ', '03-', i)
    i = re.sub('abril de ', '04-', i)
    i = re.sub('maio de ', '05-', i)
    i = re.sub('junho de ', '06-', i)
    i = re.sub('julho de ', '07-', i)
    i = re.sub('agosto de ', '08-', i)
    i = re.sub('setembro de ', '09-', i)
    i = re.sub('outubro de ', '10-', i)
    i = re.sub('novembro de ', '11-', i)
    i = re.sub('dezembro de ', '12-', i)
    i_ = re.sub('( )', '', i[5:])
    date.append(i_)

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 10000)

print(date)

dic_date = {'Postdate' : date}
df = (pd.DataFrame(dic_date))
df


# In[174]:


df.to_csv('instacocobambu.csv')


# In[216]:


tabela = pd.read_csv('instacocobambu.csv')
tabela = tabela.loc[0:,['Postdate']]
val = tabela.value_counts().reset_index()


lst_certa = []

for g in range(0,18):
    a = (str(val[g:g+1]))
    a = a[18:]
    a = a.strip(' ')
    lst_certa.append(a)
lst_certa


# In[217]:


for i in lst_certa:
#     print(i[8:])
    print(i[:8])


# In[227]:


lst_date = []
lst_val = []
val = tabela.value_counts().reset_index()
datas = tabela['Postdate'].unique()
dic_datas = {}

for d in datas:
    for v in lst_certa:
        if v[:7] == d:
            dic_datas[d] = v[8:]

for d in datas:
    lst_val.append(int(dic_datas[d]))

for d in dic_datas:
    lst_date.append(d)

dic_datas


# In[231]:


trace =go.Scatter(x = lst_date[-2::-1],
                    y = lst_val[-2::-1],
                    mode = 'markers+lines',
                    name = 'Variação do número de tweets',
                    line = {'color': '#483D8B',
                           'width' : 2})
data = [trace]
layout = go.Layout(title = 'Publicações no instagram com a localização no restaurante Coco Bambu',
                   xaxis = {'title': 'Período'},
                   yaxis = {'title': 'Publicações'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[221]:


import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)


# In[207]:


datas = [out19, nov19, dez19,jan20, fev20, mar20, abr20, mai20, jun20, 
      jul20, ago20, set20, out20, nov20, dez20, jan21, fev21, mar21,
     abr21, mai21, jun21]

datas_ = []
for i in datas:

    datas_.append(int(i))
datas_


# In[208]:


trace_meses_saraiva = go.Scatter(x = ['out19', 'nov19','dez19','jan20', 'fev20', 'mar20', 'abr20', 'mai20', 'jun20', 
      'jul20', 'ago20', 'set20', 'out20', 'nov20', 'dez20', 'jan21', 'fev21', 'mar21',
    'abr21', 'mai21'],
                    y = datas_,
                    mode = 'lines',
                    name = 'Quantidade de Posts')


data = [trace_meses_saraiva]
layout = go.Layout(title = "Posts do Intagram com localização na livraria Cultura",
                   xaxis_title = 'Mês',
                   yaxis_title = 'Posts')
fig = go.Figure(data = data, layout = layout)
py.iplot(fig)


# In[186]:


print(out19, nov19, dez19)


# In[114]:


data_cultura = []
for d in date_cultura:
    data_cultura.append(d [5:])
data_cultura


# In[116]:





# In[29]:


da_saraiva= []
for d in data_saraiva:
    if (d[-4:]) != '2019':
        da_saraiva.append(d)
da_saraiva


# In[33]:


# data = []
# for d in da_saraiva:
#     data.append(d [5:])
# data


# In[34]:


# da= []
# for d in data:
#     if (d[-4:]) != '2019':
#         da.append(d)
# da


# In[118]:





# In[35]:


mes_saraiva = []
for i in da_saraiva:
    di = (i[:-7])
    di = re.sub(' ', '', di)
    di = di[:3]
    mes_saraiva.append(di)
print(mes_saraiva)


# In[27]:


quant_mes_sa = [jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez]
mes_sa = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
quant_mes_sa


# In[37]:


import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
import numpy as np
import plotly.express as px


# In[149]:


trace_meses = go.Scatter(x = mes,
                    y = quant_mes,
                    mode = 'markers+lines',
                    name = 'Quantidade de Posts')


data = [trace_meses]
layout = go.Layout(title = "Posts do Intagram com localização no restuarante Coco Bambu",
                   xaxis_title = 'Mês',
                   yaxis_title = 'Posts')
fig = go.Figure(data = data, layout = layout)
py.iplot(fig)

