from bs4 import BeautifulSoup 
import requests

URL = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/74.0.3729.157 Chrome/74.0.3729.157 Safari/537.36'}

page = requests.get(URL, headers=headers)

#soup1 = BeautifulSoup(page.content, 'html.parser')
#soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title)
print(soup.title.string)

#print(soup.get_text())
