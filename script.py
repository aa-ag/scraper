############------------ IMPORTS ------------##################################
import requests
from bs4 import BeautifulSoup

############------------ FUNCTION(S) ------------##############################
def get_img_href_srcs(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    for img in soup.select("img"):
        print(img.get("src"))


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.zendesk.com/hc/en-us/articles/4408822236058"
    get_img_href_srcs(url)