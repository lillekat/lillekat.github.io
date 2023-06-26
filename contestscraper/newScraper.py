import requests
from bs4 import BeautifulSoup

url = input()
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find("table", class_="table2")

print("[*Kattis event*]({}) \n".format(url))

list_elem = "- [{}]({})"

for t in table.findAll('a'):
    name = t.string.strip()
    link = t['href']

    print(list_elem.format(name, "https://open.kattis.com/"+link))

print("\n")
