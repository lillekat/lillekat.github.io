# input: contest url
# output: url to first problem

import requests
from bs4 import BeautifulSoup


url = input()
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h2', class_='title')
date = soup.find('div', class_="col-md-3 text-left no-pad")
prob_elems = soup.find('table', id='standings').find_next('tr').find_all('th', class_='problemcolheader-standings')

print("## {} ({})\n".format(title.text, "datestring"))

for prob_elem in prob_elems:
    print(prob_elem.attrs)
    break
    list_elem = "- [{} ({})]({})"
    print(list_elem.format("name", "id", "url.kattis.com"))

print("\n")
