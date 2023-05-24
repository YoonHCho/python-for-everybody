''' Exercise 2:
Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
of the number of characters at the end of the document.

Test with
http://data.pr4e.org/intro.txt
http://data.pr4e.org/mbox-short.txt
http://data.pr4e.org/romeo-full.txt
'''

import socket

inStr = ''

while True:
    try:
        url = input('Enter the URL: ')
        hostName = url.split('/')[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((hostName, 80))
        url = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
        cmd = url.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            inStr += data.decode()
        mysock.close()
        break
    except:
        print("Invalid URL")

print(inStr[:3000])   # to print the first 3000 characters
print(len(inStr))   # to print the total characters
