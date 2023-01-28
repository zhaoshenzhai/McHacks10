import requests
from bs4 import BeautifulSoup
import scrape
# import re
# import pandas as pd

# Global variables
WEBSITES = {}
USERS = {}


# query = input("Query: ")
# search = query.replace(' ', '+')
q = "data science"
num_results = 20

url = (f"https://www.google.com/search?q={q}&num={num_results}")

requests_results = requests.get(url)
soup_link = BeautifulSoup(requests_results.content, "html.parser")
links = soup_link.find_all("a")

results = scrape.get_results(links)  # dict { <web link> : <web title> }
