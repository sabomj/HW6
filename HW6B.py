# # # To run this, you can install BeautifulSoup
# # # https://pypi.python.org/pypi/beautifulsoup4
# # 
# # # Or download the file
# # # http://www.py4e.com/code3/bs4.zip
# # # and unzip it in the same directory as this file
# # 
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


urllst = []
url = input('Enter - ')
x = 0 

while x < 7:
    
    taglst = []
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for i in range(8):
        for tag in tags:
            taglst.append(tag)

    url = taglst[17].get('href', None)
    urllst.append(url)

    x = x + 1  


y = re.findall('by_([^ ]*).html', url)
print (y[0])
