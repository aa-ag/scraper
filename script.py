import requests
from bs4 import BeautifulSoup

result = requests.get("https://google.com/")

# print(result.status_code)
# print(result.headers)

src = result.content
# print(src)

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
# print(links)

for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])