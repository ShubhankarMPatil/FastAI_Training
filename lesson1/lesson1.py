from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *
from time import sleep

def search_images(term, max_images = 30):
    print(f"Searching for '{term}'")
    return DDGS().images(keywords=term, max_results = max_images)

bird_urls = search_images('bird photos', max_images = 0)
forest_urls = search_images('forest photos', max_images = 7)
b_urls = list(bird_urls)
f_urls = list(forest_urls)

count = 39

for i in b_urls:
    download_url(i.get('image'), f'birds/bird_{count}.jpg', show_progress=False)
    count = count + 1
    sleep(1)

count = 44

for i in f_urls:
    download_url(i.get('image'), f'forest/forest_{count}.jpg', show_progress=False)
    count = count + 1
    sleep(1)