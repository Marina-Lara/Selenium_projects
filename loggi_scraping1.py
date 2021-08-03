#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importanto o webdriver... que vai até a web recolher as informações que precisamos
from selenium import webdriver

#agora importando a biblioteca especiaca pro chrome(que é o navegador que eu optei usar)
from selenium.webdriver import Chrome

##sleep é uma biblioteca que não faz parte do selenium mas é essencial para que o código não dê erros em alguns pontos 
#em que é essencial que haja uma pausa até carregar o contúdo da página e não haver erro 
from time import sleep

data = []
p = 1

for i in range(0, 5):
    #resumindo o trecho de código "webdriver.ChromeOptions()" em "op" para as minhas configurações do 
    #driver ficarem menos extensas
    op = webdriver.ChromeOptions()
    
    #a opção headless faz ccom que, ao rodar o código, o driver não abra a guia do navegador na sua tela e faça todo o processo
    #em segundo plano(se é que posso chamar assim)
    #op.add_argument('headless')  
    
    url = ('https://www.reclameaqui.com.br/empresa/dialogo-logistica/lista-reclamacoes/?pagina=' + str(p))
    
    #essa parte é importante.... aqui a gente define o caminho que o driver vai percorrer até chegar no chromedriver (que é
    #um software que a gente instala antes de começar a codar (o processo de inatalção é meio embassado, mas tem um vídeo
    #mto bom que foi oq funcionou pra mim que é oq o jeff colocou numa atividade la no teams chamada "primeira automação
    #com selenium" (ou algo assim) e caso você não tenha instalado acredito que ele vá  te ajudar bastante(a instalação ta no 
    #começo do vídeo)...Mas tem uma parte importante que é essa do caminho do arquivo... quando você for instalar tem que 
    #prestar atenção em onde coloca o arquivo porque depois vai ter que colocar esse caminho exato aqui embaixo:
    driver = Chrome(r"C:\Users\marin\Desktop\chrome_driver\chromedriver.exe", options=op) #mas isso também explica no vídeo
    
    driver.get(url)
    sleep(1)
    
    #aqui ja é essa sintaxe específica da biblioteca selenium... lembra a lógica do bs4, oq muda mais é o jeito de escrever
    #nesse caso pedi pra ele pegar oq está dentro das tags de calsse 'hourAgo.ng-binding'
    data_text = driver.find_elements_by_class_name('hourAgo.ng-binding')
    
#     print(data_text)
    for d in data_text:
        data.append(d.text)
        
    print('página {}: lida'.format(p))
    p += 1
print(data)
# tabela_data = {'Data' : data}
# print(tabela_data)

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df= pd.DataFrame({'Data' : data})
display(df)


# In[17]:


pd.set_option('display.max_rows', 540)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#display(df)

c = df[112::]
b = c.value_counts().reset_index()
display(b)



# In[2]:




