from urllib.parse import urljoin , urlparse
import requests
from bs4 import BeautifulSoup

all_links = set()
home_url = "https://loksatta.com"

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    base_link = "loksatta.com"
    links = set()
    for a_tag in soup.find_all('a' , href=True):
        link = a_tag['href']
        full_link = urljoin(url , link)
        if base_link in urlparse(full_link).netloc:
            all_links.add(full_link)
            links.add(full_link)
    return links


def add_links(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    base_link = "loksatta.com"

    for a_tag in soup.find_all('a' , href=True):

        link = a_tag['href']
        full_link = urljoin(home_url , link)

        if base_link in urlparse(full_link).netloc:
            all_links.add(full_link)

def save_links(links,filename="loksattalinks.txt"):

    with open(filename , "w" , encoding="utf-8") as file:

        for link in links:
            file.write(link +"\n")


if __name__ == "__main__":

    url = "https://loksatta.com"

    links = get_links(url)


    for url in links:
        add_links(url)
    
    save_links(all_links)
    print(f"Total links ---> {len(all_links)}")
    print("File saved!!")
