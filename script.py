############------------ IMPORTS ------------##################################
import requests
from bs4 import BeautifulSoup

############------------ FUNCTION(S) ------------##############################
def scrape_images(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    for img in soup.select("img"):
        print(img.get("src"))


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.apple.com/mac/macbook-pro"
    scrape_images(url)