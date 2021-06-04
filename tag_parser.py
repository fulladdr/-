#!/usr/bin/env python
# coding: utf-8

# In[5]:


import selenium
from selenium import webdriver
import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup


# In[10]:


html = "" #local에 저장한 html 주소값 넣어주시면 됩니다
driver = webdriver.Chrome("")
driver.get(html)
file = open(html, "r", encoding = "utf-8")
soup = BeautifulSoup(file, "html.parser")

total_tag = 0
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")


with open('./feature.xls', 'r') as f:
    while True:
        feature = f.readline().rstrip()
        if not feature: break
        data = soup.findAll(feature)
        numbers = [d.text for d in data]
        if len(numbers) == 0 : continue
        print("The number of tag <%s> is %d"%(feature,len(numbers)))
        total_tag += 1
        
print("\nTotal tag in html %s is %d"%(html, total_tag))

time = domComplete - responseStart
print("Total time is : %.20f" %time)


# In[25]:




