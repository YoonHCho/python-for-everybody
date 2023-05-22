''' Exercise 1:
Change the socket program socket1.py to prompt the user for the URL so it can read
any web page. You can use split('/') to break the URL into its component parts so
you can extract the host name for the socket connect call. Add error checking using
try and except to handle the condition where the user enters an improperly formatted
or non-existent URL.

check with following URLS:
http://data.pr4e.org/intro-short.txt
http://data.pr4e.org/romeo.txt
http://data.pr4e.org/clown.txt
http://data.pr4e.org/words.txt
'''

import socket

theURL = input("Please Enter URL: ")

try:
    hostName = theURL.split('/')[2]
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((hostName, 80))
    req = 'GET ' + theURL + ' HTTP/1.0\r\n\r\n'
    cmd = req.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1:
            break
        print(data.decode())
    mysocket.close()
except:
    print("Invalid URL, improperly formatted or non-existent")
