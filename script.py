############------------ IMPORTS ------------##################################
import requests
from bs4 import BeautifulSoup

############------------ FUNCTION(S) ------------##############################
def get_img_href_srcs(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    return [
        img.get("src") for img in soup.select("img")
        if "https://" in img.get("src")
    ]


def download_files(img_srcs):
    
    for img_src in img_srcs:
        file_name = img_src.split("/")[-1]
        print(file_name)
        # r = requests.get(img_src, stream=True)

        # print(r.status_code)
        


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.zendesk.com/hc/en-us/articles/4408822236058"
    img_srcs = get_img_href_srcs(url)
    download_files(img_srcs)