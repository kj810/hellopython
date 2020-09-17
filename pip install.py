# 구글에서 pypi를 검색. BeautifulSoup 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print (soup.prettify())