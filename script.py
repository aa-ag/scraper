############------------ IMPORTS ------------##################################
import requests
from bs4 import BeautifulSoup

############------------ FUNCTION(S) ------------##############################
def get_img_href_srcs(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    return [
        img.get("src") for img in soup.select("img")
    ]


def download_files(img_srcs):
    pass


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.zendesk.com/hc/en-us/articles/4408822236058"
    img_srcs = get_img_href_srcs(url)
    download_files(img_srcs)