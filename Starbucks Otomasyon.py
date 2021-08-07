# Kahve Otomasyonu: Kullanıcınn isteğine göre içecek veya yiyecek menüsü sunulur
# Web Scraping metodu kullanılarak Starbucks sitesinden içecek ve yiyecek menüsü çekilir

import pandas as pd     
import time
from urllib.request import urlopen  
from bs4 import BeautifulSoup  
import re  


icecekler = "https://www.starbucks.com.tr/menu-list/beverage-list/espresso-bazli-icecekler"
html = urlopen(icecekler)
soup = BeautifulSoup(html, "html.parser")

yiyecekler = "https://www.starbucks.com.tr/menu-list/food-list/cheesecake-ve-pastalar"
html2 = urlopen(yiyecekler)
soup2 = BeautifulSoup(html2, "html.parser")

allrows = soup.find_all("span")
allrows2 = soup2.find_all("span")

print("Starbucks'a Hoş Geldiniz!")
time.sleep(0.5)
soru = int(input("İçeceklere mi Yiyeceklere mi Baktınız? (1/2): "))

if soru == 1:
    for cell in allrows[:32]:
        print(cell.text)
        time.sleep(0.3)
    hangi = str(input("Hangi İçeceği İstersiniz?: "))
    time.sleep(0.3)
    print("İçeceğiniz Hazırlanıyor...")
    time.sleep(3)
    pipet = int(input("Pipet İster Misiniz? (0/1): ")) # 0 = hayır | 1 = evet
    if pipet == 0:
        time.sleep(0.5)
        print("İçeceğinizi Alabilirsiniz.")
    elif pipet == 1:
        time.sleep(3) 
        # pipet koyuldu
        print("İçeceğinizi Alabilirsiniz.")

elif soru == 2:
    for cell2 in allrows2[:14]:
        print(cell2.text)
        time.sleep(0.4)
    hangi2 = str(input("Hangi Yiyeceği İstersiniz?: "))
    time.sleep(0.5)
    print("Yiyecek Hazırlanıyor...")
    time.sleep(5)
    print("Yiyeceğinizi Alabilirsiniz.")