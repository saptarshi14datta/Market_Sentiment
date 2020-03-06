import requests
from bs4 import BeautifulSoup
import os
import json
from datetime import datetime
import math
import pandas as pd
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

#options = webdriver.ChromeOptions()
#browser = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe',chrome_options=options)


url_1 = "https://business.financialpost.com/category/news"
url_2 = "https://www.investopedia.com/news-4427706"
url_3 = "https://www.marketwatch.com/"
url_4 = "https://finviz.com/news.ashx"
url_5 = "https://www.bloomberg.com/markets"
url_6 = "https://www.marketwatch.com/"
url_7 = "https://www.marketwatch.com/"
url_8 = "https://www.marketwatch.com/"
url_9 = "https://www.marketwatch.com/"
url_10 = "https://www.marketwatch.com/"

page = requests.get(url_5)
soup = BeautifulSoup(page.content, 'html.parser')
#headlines = soup.find_all('a', class_='nn-tab-link')

"""
#FINVIZ
news_link=[]
for elem in soup.find_all("a", {"class":"nn-tab-link"}):
    news_link.append(elem.text)

list_exclusion = math.floor(len(news_link)*0.05)
news_link = news_link[list_exclusion:-list_exclusion]
articles = pd.DataFrame(news_link,columns=['Headlines'])

#Investopedia
news_link=[]
for elem in soup.find_all("h4", {"class":"card__title"}):
    news_link.append(elem.text)
"""

#Bloomberg
news_link=[]
for elem in soup.find_all("h3", {"class":"story-package-module__story__headline"}):
    news_link.append(elem.text)




print("z")

'''
url = [url_1, url_2, url_3, url_4, url_5, url_6, url_7, url_8, url_9, url_10]

for i in url:
    page = requests.get(i)


articles['Date']= str(datetime.today().strftime('%Y-%m-%d'))
'''