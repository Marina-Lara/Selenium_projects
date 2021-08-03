#!/usr/bin/env python
# coding: utf-8

# In[220]:


#codigo geral

from selenium import webdriver
import pandas as pd
from time import sleep

status = []
titulo = []
localizacao = []
data = []
p = 1
for pagina in range(0,66):
    url = 'https://www.reclameaqui.com.br/empresa/dialogo-logistica/lista-reclamacoes/?pagina=' + str(pagina)
    driver = webdriver.Chrome(r"C:\Users\Desktop\Documents\PUC\Aplicativos\chromedriver\chromedriver.exe")
    driver.get(url)
    sleep(3)
    status_text = driver.find_elements_by_class_name('company-complain-status')
    titulo_text = driver.find_elements_by_class_name('title-holder')
    localizacao_text = driver.find_elements_by_class_name('hidden-xs ng-binding')
    data_text = driver.find_elements_by_class_name('hourAgo ng-binding')
    for s in status_text:
        status.append(s.text)

    for t in titulo_text:
        titulo.append(t.text)

    for l in localizacao:
        localizacao.append(l.text)

    for d in data:
        data.append(d.text)

    print('página {}: lida'.format(p))
    p += 1

print('fim')


# In[221]:


#expandindo tabela geral
import pandas as pd
tabela = pd.read_csv('tabela_diallogistica.csv', sep = ",")
display(tabela)


# In[228]:


##extraindo reclamações resolvidas 
s = tabela.loc[tabela['Status'] == 'Resolvido']
display(s)


# In[246]:


#contando quantas vezes que o status é resolvido
s1 = s['Status'].value_counts()
display(s1)


# In[251]:


#removendo valores nulos
s.dropna()


# In[239]:


#filtrando comos tipos de problemas, por meio das palavras chaves

#entregador
motoboy = []
conta = []
stext = s.values
for i in stext:
    b = 'motoboy' in str(i).lower()
    if b == True:
        motoboy.append(i)
for i in stext:
    b = 'entregador' in str(i).lower()
    if b == True:
        motoboy.append(i)
c = len(motoboy)
conta.append(c)
print('Problemas com o entregador:{}'.format(c))


#valor
preço = []
for i in stext:
    b = 'valor' in str(i).lower()
    if b == True:
        preço.append(i)
for i in stext:
    b = 'preço' in str(i).lower()
    if b == True:
        preço.append(i)
for i in stext:
    b = 'cobra' in str(i).lower()
    if b == True:
        preço.append(i)
for i in stext:
    b = 'dinheiro' in str(i).lower()
    if b == True:
        preço.append(i)
for i in stext:
    b = 'aprova' in str(i).lower()
    if b == True:
        preço.append(i)
for i in stext:
    b = 'estorno' in str(i).lower()
    if b == True:
        preço.append(i)
c = len(preço)
conta.append(c)
print('Problemas em relação a valor e cobrança :{}'.format(c))


#conta
cont = []
for i in stext:
    b = 'conta' in str(i).lower()
    if b == True:
        cont.append(i)
for i in stext:
    b = 'usuário' in str(i).lower()
    if b == True:
        cont.append(i)
for i in stext:
    b = 'cadastr' in str(i).lower()
    if b == True:
        cont.append(i)
for i in stext:
    b = 'código' in str(i).lower()
    if b == True:
        cont.append(i)
c = len(conta)
conta.append(c)
print('Problema com cadastro:{}'.format(c))

#atraso
atraso = []
for i in stext:
    b = 'dias' in str(i).lower()
    if b == True:
        atraso.append(i)
for i in stext:
    b = 'demor' in str(i).lower()
    if b == True:
        atraso.append(i)
for i in stext:
    b = 'ainda' in str(i).lower()
    if b == True:
        atraso.append(i)
for i in stext:
    b = 'tempo' in str(i).lower()
    if b == True:
        atraso.append(i)
for i in stext:
    b = 'atras' in str(i).lower()
    if b == True:
        atraso.append(i)
c = len(atraso)
conta.append(c)
print('Problemas com atraso: {}'.format(c))

#atendimeto
atendimento = []
for i in stext:
    b = 'atendi' in str(i).lower()
    if b == True:
        atendimento.append(i)
for i in stext:
    b = 'respeito' in str(i).lower()
    if b == True:
        atendimento.append(i)
for i in stext:
    b = 'cliente' in str(i).lower()
    if b == True:
        atendimento.append(i)
c = len(atendimento)
conta.append(c)
print('Problemas em relação a atendimento: {}'.format(c))

#roubo
furto = []
for i in stext:
    b = 'furt' in str(i).lower()
    if b == True:
        furto.append(i)
for i in stext:
    b = 'roub' in str(i).lower()
    if b == True:
        furto.append(i)
for i in stext:
    b = 'desapareceu' in str(i).lower()
    if b == True:
        furto.append(i)
for i in stext:
    b = 'sumiu' in str(i).lower()
    if b == True:
        furto.append(i)
c = len(furto)
conta.append(c)
print('Problemas com relação a furto:{}'.format(c))


# In[238]:


#transformando em gráfico
import numpy as np
import matplotlib.pyplot as plt

tipos_de_problema = ['Entregador', 'Valor e cobrança', 'Cadastro', 'Atraso', 'Atendimento', 'furto']
quantidade = [5,0,2,45,1,2]

plt.barh(tipos_de_problema, quantidade, color='orange')

plt.ylabel("Problemas")
plt.xlabel("Quantidade")
plt.title("GRÁFICO")

plt.show()


# In[ ]:




