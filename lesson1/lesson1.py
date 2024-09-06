from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *

def search_images(term, max_images = 30):
    print(f"Searching for '{term}'")
    return DDGS().images(keywords=term, max_results = max_images)

urls = search_images('bird photos', max_images = 100)
urls = list(urls)

for i in urls:
    # download_url(i.get('image'), 'bird.jpg', show_progress=False)
    # im = Image.open('bird.jpg')
    # im.to_thumb(256, 256)

    print(i.get('image'))