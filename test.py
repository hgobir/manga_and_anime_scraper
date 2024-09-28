from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('\nIt worked!')
    print(html.read())

# bs = BeautifulSoup(html, 'html.parser')
    bs = BeautifulSoup(html, 'lxml')

    print(bs.h1)