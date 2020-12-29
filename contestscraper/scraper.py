import requests
import re
from bs4 import BeautifulSoup


url = input()
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h2', class_='title')
prob_elems = soup.find('table', id='standings').find_next('tr').find_all('a')

print("[*Kattis event*]({}) \n".format(url))
# alt title
#print("## {} \n".format(title.text))

list_elem = "- [{}]({})"

for prob_elem in prob_elems:
    name = prob_elem['title']
    id = re.findall("/([^/]*)$",prob_elem['href'])[0]
    print(list_elem.format(name, "https://open.kattis.com/problems/"+id))

print("\n")
