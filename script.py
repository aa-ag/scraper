############------------ IMPORTS ------------##################################
import requests

############------------ FUNCTION(S) ------------##############################
def scrape_images(url):
    r = requests.get(url)
    print(r.status_code)

############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    url = "https://support.apple.com/mac/macbook-pro"
    scrape_images(url)