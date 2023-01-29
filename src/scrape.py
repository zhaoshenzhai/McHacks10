import re
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/91.0.4472.114 Safari/537.36'}

def get_links(subreddit):
    links = []

    page = requests.get("https://old.reddit.com/r/" + subreddit + "/", headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    domains = soup.find_all("a", class_ = "comments", href = True)
    for domain in domains:
        links.append(domain['href'])

    return links

def get_sentences(url):
    comments = []
    sentences = []
    
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    domains = soup.find_all("div", class_ = "usertext-body")
    for domain in domains:
        comments.append(domain.text.replace("\n", ""))
    
    comments = comments[2:]
    for c in comments:
        res = re.split('[.?!]', c)
        res = res[:-1]
        for r in res:
            if r != '':
                sentences.append(r.strip())

    return sentences
