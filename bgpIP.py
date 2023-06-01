import requests
import argparse
from bs4 import BeautifulSoup
def scraper():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', required=True, default=False, metavar='search term', type=str)
  parser.add_argument('-k', required=True, default=False, metavar='keyword to filter eg.: Dell, Inc.', type=str)
  args = parser.parse_args()
  Headers = ({'User-Agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
      (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
      'Accept-Language': 'en-US, en;q=0.5'})
  res = requests.get(f"https://bgpview.io/search/{args.u}#results-v4",Headers)
  soup = BeautifulSoup(res.text,features="html.parser")
  for tr in soup.find_all('tr'):
     if args.k in str(tr):
        for i in tr.find_all('td'):
            t= i.find('a')
            if t == None or "AS" in str(t.next):
               continue
            else:
               print(t.next)
if __name__ == '__main__':
    scraper()
