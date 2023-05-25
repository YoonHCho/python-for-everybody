''' Exercise 4:
Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the
paragraphs as the output of your program. Do not display the paragraph text, only count them. Test your program on several
small web pages as well as some larger web pages.

Tested
https://beautiful-soup-4.readthedocs.io/en/latest/
https://example.com/
https://online.dr-chuck.com/
'''

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
# Retrieve all of the paragraph tags
tags = soup('p')
for tag in tags:
    count += 1

print('Number of Paragraphs: ', count)
