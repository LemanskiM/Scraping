#!/usr/bin/env python
# coding: utf-8

# In[67]:


from bs4 import BeautifulSoup
import requests
import re

search_term = ("Gaming Desktop")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
	url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
	page = requests.get(url).text
	doc = BeautifulSoup(page, "html.parser")

	div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
	items = div.find_all(text=re.compile(search_term))

	for item in items:
		parent = item.parent
		if parent.name != "a":
			continue

		link = parent['href']
		next_parent = item.find_parent(class_="item-container")
		try:
			price = next_parent.find(class_="price-current").find("strong").string
			items_found[item] = {"price": int(price.replace(",", "")), "link": link}
		except:
			pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

x = []
y = []

for item in sorted_items:
#	print(item[0])
	x.append(item[0])
	y.append(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")
print(x)


# In[14]:


df = x


# In[9]:


df


# In[10]:


import pandas as pd


# In[68]:


yf = pd.DataFrame(data =y)
xf = pd.DataFrame(data =x)


# In[69]:


df = pd.DataFrame({"cena":y, "name":x})


# In[70]:


df


# In[71]:


x


# In[ ]:




