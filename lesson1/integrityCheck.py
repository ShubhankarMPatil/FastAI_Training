from duckduckgo_search import DDGS
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *
from time import sleep

count = 0

while count < 49:
    failed = verify_images(get_image_files(f"birds/birds_{count}.jpg"))
    failed.map(Path.unlink)
    count+=1;

len(failed)