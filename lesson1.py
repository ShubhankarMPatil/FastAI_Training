from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *
from time import sleep

def search_images(term, max_images = 30):
    print(f"Searching for '{term}'")
    return DDGS().images(keywords=term, max_results = max_images)

urls = search_images('bird photos', max_images = 10)
urls = list(urls)

count = 0

for i in urls:
    download_url(i.get('image'), f'bird {count}.jpg', show_progress=False)
    count = count + 1
    sleep(10)