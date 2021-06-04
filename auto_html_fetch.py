#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pyautogui
import time
import os
import os.path
import shutil
import pyperclip
import requests

import csvTju

urls = []
names=[]


# In[ ]:


import selenium
from selenium import webdriver
import urllib
import urllib.request
from bs4 import BeautifulSoup


# In[2]:


with open('./target.csv','r') as f: 
    reader = csv.reader(f)
    for txt in reader: 
        urls.append("http://"+txt[0]+"/")

for url in urls:
    if 'porn' in url:
        urls.remove(url)
    if 'sex' in url:
        urls.remove(url)
    if 'xvideos' in url:
        urls.remove(url)
    if 'xhamster' in url:
        urls.remove(url)
    if 'xx' in url:
        urls.remove(url)
print(urls)


# In[ ]:



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r"C:/Users/Admin/Desktop/webpage",
  "download.prompt_for_download": False,
  "download.directory_upgrade": False,
  "safebrowsing.enabled": True
})

for url in urls:
    print(url)
    try:
        response = requests.get(url,timeout=10)
    
    except requests.exceptions.Timeout:
        continue
    except requests.exceptions.ConnectionError:
        continue
    except requests.exceptions.HTTPError:
        continue
    except requests.exceptions.RequestException:
        continue
    except requests.Timeout:
        continue
    except Exceptions:
        continue
    if response.ok:
        print("OK")
        driver = webdriver.Chrome(options=chrome_options, executable_path='C:/Users/Admin/Desktop/webpage/chromedriver')
        driver.get(url)
        # Web loading time 최대 100sec
        driver.implicitly_wait(10)
        # MACOS : command/s, command/c-------------- Windows : ctrl/s, ctrl/c
        pyautogui.hotkey('ctrl','s')
        time.sleep(1)
        pyautogui.hotkey('ctrl','c')
        time.sleep(0.5)
        # time sleep이 없다면 이전 명령어가 실행되기 이전에 다음 명령어가 실행될 수 있습니다. 만약 이런 현상이 발생한다면 time sleep을 늘려주세요.
        pyautogui.press('enter')
        names.append(pyperclip.paste())
    


# In[35]:


print(names)
print(len(names))


# In[37]:


temp = set(names)
names = list(temp)
for tmp in names:
    print(tmp)
    # path: 새로운 디렉토리를 만들어줄 경로를 설정해주시면 됩니다
    path = 'C:/Users/Admin/Desktop/webpage/{}'.format(tmp)
    os.mkdir(path)
    # src_file : chrome을 selenium을 통해서 돌릴 때 cmd/s때 기본적으로 저장되는 경로 + filename
    src_file = 'C:/Users/Admin/Downloads/{}.html'.format(tmp)
    # dest_file : 이전에 만들어준 디렉토리의 경로 + filename
    dest_file = 'C:/Users/Admin/Desktop/webpage/{}/{}.html'.format(tmp, tmp)
    # src_directory : 위와 동일 + directory_name
    src_directory = 'C:/Users/Admin/Downloads/{}_files'.format(tmp)
    # dest_directory : 위와 동일 + directory_name
    dest_directory = 'C:/Users/Admin/Desktop/webpage/{}/{}_files'.format(tmp, tmp)
    
    
    # 원하는 파일이 생성되기 이전까지 lock (files디렉토리는 생성이 되지 않는 경우도 있을 수 있어 file의 유무만 확인)
    if os.path.exists(dest_file): # or not os.path.exists(src_directory): 
        continue    
    
    shutil.move(src_file, dest_file)
    shutil.move(src_directory, dest_directory)


# In[ ]:




