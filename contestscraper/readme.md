# read me

To use the contest-problem-to-markdown-list-generator you will need to install python as well as the libraries `BeautifulSoup` and `requests`.

```
pip3 install BeautifulSoup
pip3 install requests
```

Then run the script and enter the full url of the contest in question

```
python scraper.py
https://open.kattis.com/contests/exampleContestID
```

## to do

- [x] simply read a url of problem from the contest html
- [ ] check correct url
- [ ] check response 200
- [x] print list of problem urls
- [x] print list w. name and link to problem
  - [x] find the name of the problem
  - [x] format url
- [ ] add option to append to existing markdown file
- [ ] add formatting to automatically add photos based on date and yyyymmdd.png naming convention
