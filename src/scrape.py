import requests
from bs4 import BeautifulSoup
# import re
# import pandas as pd


# query = input("Query: ")
# search = query.replace(' ', '+')
q = "data science"
num_results = 1
url = (f"https://www.google.com/search?q={q}&num={num_results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
links = soup_link.find_all("a")

result = {}


for link in links:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        title = link.find_all('h3')
        if len(title) > 0:
            # result[link.get('href').split("?q=")[1].split("&sa=U")[0]] = {title: title[0].getText()}
            web_link = link.get('href').split("?q=")[1].split("&sa=U")[0]
            web_ttl = title[0].getText()  # title of the website
            print(web_link)
            print(web_ttl)
            print("------")
