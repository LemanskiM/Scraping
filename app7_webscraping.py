#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Please execute this cell first to have the headers ready
# Some websites need to see some browser headers to allow scripts to scrape them.
# Such headers can be found on Google and then be used in requests.get() as we do in this notebook

#pip install beautifulsoup4
#pip install pandas

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


# In[2]:


#Get the first page to extract page numbers
import requests, re
from bs4 import BeautifulSoup

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers) # We use the headers here
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr,"number of pages were found")


# In[3]:


l=[]
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print( )
    r=requests.get(base_url+str(page)+".html", headers=headers)
    c=r.content
    #c=r.json()["list"]
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
        except:
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Full Baths"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None
        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    print(feature_name.text)
                    d["Lot Size"]=feature_name.text
        l.append(d)


# In[4]:


l


# In[5]:


import pandas
df=pandas.DataFrame(l)


# In[6]:


df


# In[7]:


df.to_csv("Output.csv")


# In[18]:


import requests, re
from bs4 import BeautifulSoup

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers=headers)
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr,"number of pages were found")

base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print( )
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    #c=r.json()["list"]
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})

print(all)
