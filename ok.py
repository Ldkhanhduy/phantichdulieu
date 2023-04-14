import requests
from bs4 import BeautifulSoup

ga = requests.get("http://www.vncreatures.net/chitiet.php?page=1&loai=1&ID=5567")
ga = BeautifulSoup(ga.content,"html.parser")
print(ga)