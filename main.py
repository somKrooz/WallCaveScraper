from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from bs4 import BeautifulSoup
import requests
from downloader import download
import random

path = "images"
for i in os.listdir(path):
    pathhh = os.path.join(path,i)
    os.remove(pathhh)

def download(ur):
    res = requests.get(ur)
    with open(f"images/image{random.randint(0, 100)}.png", "wb") as f:
        f.write(res.content)

def Scape():
    state = input("enter a valid wallpaper cave url:  ")
    num = int(input("num: "))
    
    ser = Service(executable_path="C:/Users/somkr/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    # chrome_options = Options()
    driver = webdriver.Chrome(service=ser)
    driver.get(f"{state}")
    time.sleep(1)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    images = soup.find_all('img')
    url = []
    for img in images:
        if str(img.get('src')).endswith("jpg"):
            urls = f"https://wallpapercave.com{img.get('src')}"
            url.append(urls)

    driver.quit()
    print(url)
    for i in url[:num]:
        download(i)


if __name__ == "__main__":
    Scape()

