#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# In[ ]:


# connect to website

URL = 'https://www.jumia.com.ng/hp-elite-dragonfly-g4-intel-core-i7-1365u-1tb-ssd-32gb-ram-face-id-fp-reader-backlit-keyboard-13.5-fhd-touchscreen-win-11-pro-270705379.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}


page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(class="-fs20 -pts -pbxs").get_text()

price = soup2.find(class="-b -ltr -tal -fs24 -prxs" ).get_text()

print(title)


# In[ ]:


price = price.strip()[1:]
tiltle = title.strip()



# In[ ]:


import datetime

today = datetime.day.today()

print(today)


# In[ ]:


import cs
header = ['title', "price", 'date']
data = [title, price, today]
with open (Jumiawebscraperdataset.csv', 'w', newlines", encoding="UTF8") as f:
    writer csv.writer()
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:


import pandas as pd
df = pd.read_csv(r "C:\Users\fred\Jumiawebscraperdataset.csv")
print (df)


# In[ ]:


#Now we are appending data to the csv
with open('Jumiawebscraperdataset.csv', 'at', newline="', encoding="UTF8") as f:
    writer csv.writer (f)
    writer.writerow(header)
    writer.writerow(data)


# In[ ]:


def check price():
    URL = 'https://www.jumia.com.ng/hp-elite-dragonfly-g4-intel-core-i7-1365u-1tb-ssd-32gb-ram-face-id-fp-reader-backlit-keyboard-13.5-fhd-touchscreen-win-11-pro-270705379.html'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    page = requests.get (URL, headers=headers)
    soup1 = BeautifulSoup (page.content, "html.parser")
    soup2 = BeautifulSoup (soup1.prettify(), "html.parser")
    title = soup2.find(id='product Title').get_text()
    price = soup2.find(id='priceblock_ourprice').get_text()
    
    price = price.strip() [1:]
    title = title.strip()
               
    import datetime
    
    today = datetime.date.today()
 
    import cs
    header = ['title', "price", 'date']
    data = [title, price, today]
    with open (Jumiawebscraperdataset.csv', 'w', newlines", encoding="UTF8") as f:
    writer csv.writer(f)
    writer.writerow(data)


# In[ ]:


while(True):
    check_price() I
    time.sleep (86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r "C:\Users\fred\Jumiawebscraperdataset.csv")

print(df)

