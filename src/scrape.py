import requests
from bs4 import BeautifulSoup

def get_links(query, num_results):
    """
    :param query: str
    :param num_results: int
    :return: links --> used in function get_results
    """
    search = query.replace(' ', '+')
    url = (f"https://www.google.com/search?q={search}&num={num_results}")
    requests_results = requests.get(url)
    soup_link = BeautifulSoup(requests_results.content, "html.parser")
    return soup_link.find_all("a")

def get_results(links):
    """
    :param links: bs4.element.ResultSet
    :return: results : dict { <web link> : <web title> }
    """
    # to_print = ""
    results = {}
    for link in links:
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            title = link.find_all('h3')
            if len(title) > 0:
                web_link = link.get('href').split("?q=")[1].split("&sa=U")[0]
                web_ttl = title[0].getText()  # title of the website
                # to_print += (web_link + "\n"  + web_ttl + "\n\n")
                results[web_link] = web_ttl
    return results
