import requests
import random
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_url(url):
    response = requests.get(url)
    with open(f"image{random.randint(0, 100)}.png", 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    
def send_requests(urls):
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(fetch_url, urls))

    return results

def download(urls):
    results = send_requests(urls)   