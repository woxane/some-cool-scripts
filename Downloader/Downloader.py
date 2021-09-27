#!/usr/bin/python3

from tqdm import tqdm 
import requests


url = input("Enter your link : ")

file_name = input("please enter name for file : ")

url_response = requests.get(url , stream = True ) 
file_size = int(url_response.headers.get("Content-Length", 0))

progress = tqdm(url_response.iter_content(1024), f"Downloading {file_name}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
with open(file_name , "wb") as file : 
    for data in progress.iterable : 
        file.write(data) 
        progress.update(len(data))
