#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from time import sleep
import csv
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


# In[2]:


driver = Chrome()


# In[3]:


def get_tweet_data(card):
    username = card.find_element_by_xpath('.//span').text
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
        
    except NoSuchElementException:
        return
    
    tweet = (username, postdate)
    return tweet




driver.get('https://twitter.com/login')
sleep(5)

username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys('MarinaL81456103')

my_password = getpass()
sleep(2)
password = driver.find_element_by_xpath('//input[@name="session[password]"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)


# In[4]:


search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
search_input.send_keys('#cocobambu')
search_input.send_keys(Keys.RETURN)


# In[5]:


def scroll_down_page(driver, last_position, scroll_attempt=0, max_attempts=5): 
    end_of_scroll_region = False
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(num_seconds_to_load)
    curr_position = driver.execute_script("return window.pageYOffset;")
    if curr_position == last_position:
        if scroll_attempt < max_attempts:
            end_of_scroll_region = True
        else:
            scroll_down_page(last_position, curr_position, scroll_attempt + 1)
    last_position = curr_position
    return last_position, end_of_scroll_region


# In[1]:


sleep(2)
driver.find_element_by_link_text('Latest').click()

#get all tweets in the page
data = []
tweet_ids = set()
last_position = driver.execute_script('return window.pageYOffset;')
sleep(1)
scrolling = True

while scrolling:
    sleep(1)
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    sleep(2)
    for card in page_cards:
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                data.append(tweet)
    sleep(1)
    scroll_attempt = 0
    
    end_of_scroll_region = False
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(0.5)
    curr_position = driver.execute_script("return window.pageYOffset;")
    if curr_position == last_position:
        if scroll_attempt < max_attempts:
            end_of_scroll_region = True
        else:
            scroll_down_page(last_position, curr_position, scroll_attempt + 1)
    last_position = curr_position
    


# In[4]:


date = []
for i in data:
    date.append(i[1][0:7])

dic_date = {'Postdate' : date}
df = (pd.DataFrame(dic_date))


# In[57]:


df.to_csv('tweets_cocobambu.csv')


# In[3]:


tabela = pd.read_csv('tweets_cocobambu.csv')
# tabela = tabela.loc[0:,['Postdate']]
tabela


# In[261]:


lst_date = []
lst_val = []
val = tabela.value_counts().reset_index()
datas = tabela['Postdate'].unique()
dic_datas = {}

for d in datas:
    for v in lst_certa:
        if v[0:7] == d:
            dic_datas[d] = v[8:]

for d in datas:
    lst_val.append(int(dic_datas[d]))

for d in dic_datas:
    lst_date.append(d)


# In[280]:


trace =go.Scatter(x = lst_date[1:],
                    y = lst_val[1:],
                    mode = 'markers+lines',
                    name = 'Variação do número de tweets',
                    line = {'color': '#483D8B',
                           'width' : 2})
data = [trace]
layout = go.Layout(title = 'Publicações no twitter com #cocobambu',
                   xaxis = {'title': 'Período'},
                   yaxis = {'title': 'Publicações'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


# In[253]:


import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

