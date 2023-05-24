''' Exercise 3:
Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don`t worry about the headers for this exercise, simply show the first 3000
characters of the document contents.

Test with
http://data.pr4e.org/intro.txt
http://data.pr4e.org/mbox-short.txt
http://data.pr4e.org/romeo-full.txt
'''

import urllib.request
import urllib.parse
import urllib.error

inStr = ''

while True:
    try:
        url = input('Enter the URL: ')
        fhandle = urllib.request.urlopen(url)
        for line in fhandle:
            inStr += line.decode()
        break
    except:
        print("Invalid URL")

print(inStr[:3000])
print(len(inStr))
