from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://ytang913.github.io/"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser') 

items = html_soup.find_all('div', class_ = "post-wrapper")

filename = "projects.csv"
f = open(filename,'w')

headers = 'Title, Description \n'

f.write(headers)

for item in items:
    title = item.find('h6' , class_ = "post-title").text
    description = item.find('p', class_ = "post-intro").text

    f.write(title + ',' + description)

f.close()

