#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import re

#search_term = ("2")

url = "https://ogloszenia.trojmiasto.pl/remonty-budowlane/?strona=3"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
print(doc)


# In[18]:


page_text = doc.find_all(class_="list__item__details__description__text")
page_link = doc.find_all(class_ = "list__item__content__title__name")


# In[24]:



page_link[3].string


# In[25]:


page_text[3].string


# In[ ]:




