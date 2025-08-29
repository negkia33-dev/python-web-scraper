import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline a")

for t in titles:
    print(t.get_text(), "-", t["href"])
