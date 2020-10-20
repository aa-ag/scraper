import requests
from bs4 import BeautifulSoup

# result = requests.get("https://google.com/")
# result = requests.get("https://www.whitehouse.gov/briefings-statements/")
input = input("Enter a url: ")
result = requests.get(input)

# print(result.status_code)
# print(result.headers)

src = result.content
# print(src)

soup = BeautifulSoup(src, 'lxml')

# links = soup.find_all("a")
# print(links)

# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])

urls = []
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls[0])