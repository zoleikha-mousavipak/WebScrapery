import requests
from bs4_search import BeautifulSoup


search = input("Enter search item: ")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text)
print(soup.prettify())