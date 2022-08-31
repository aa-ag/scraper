############------------ IMPORTS ------------##################################
from fileinput import filename
import requests
from bs4 import BeautifulSoup

############------------ FUNCTION(S) ------------##############################
def get_img_href_srcs(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    img_srcs = [
        img.get("src") for img in soup.select("img")
        if "https://" in img.get("src")
    ]

    print(f"Found {len(img_srcs)} img srcs.")

    return img_srcs


def download_files(img_srcs):
    count = 0
    
    for img_src in img_srcs:
        
        file_name = img_src.split("/")[-1]

        r = requests.get(img_src, stream=True)

        if r.status_code == 200:
            with open(f"files/{file_name}", "wb") as f:
                for chunk in r.iter_content():
                    f.write(chunk)
            count += 1

    print(f"Downloaded {count} files.")
        


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.zendesk.com/hc/en-us/articles/4408822236058"
    img_srcs = get_img_href_srcs(url)
    download_files(img_srcs)