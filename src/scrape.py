import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


query = input("Query: ")
search = query.replace(' ', '+')
results = 20
url = (f"https://www.google.com/search?q={search}&num={results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
links = soup_link.find_all("a")

results = {}

for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        title = link.find_all('h3')
        if len(title) > 0:
            #results[link.get('href').split("?q=")[1].split("&sa=U")[0]] = {title:title[0].getText()}
            print(link.get('href').split("?q=")[1].split("&sa=U")[0])
            print(title[0].getText())
            print("------")


