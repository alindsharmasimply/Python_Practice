from urllib import *
from bs4 import *


html = urlopen("https://www.wikipedia.org")
ob = BeautifulSoup(html.read(),"html.parser")

print ob.head