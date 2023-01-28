import scrape
# import re
# import pandas as pd

# Global variables
WEBSITES = {}
USERS = {}

query = "mcgill"
num_results = 20

links = scrape.get_links(query, num_results)
results = scrape.get_results(links)  # dict { <web link> : <web title> }

print(results)
