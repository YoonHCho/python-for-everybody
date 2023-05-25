''' Exercise 5:
(Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received.
Remember that recv receives characters (newlines and all), not lines.

'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

inByteStr = b''  # need to save the data in byte-string

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    inByteStr += data

mysock.close()
# split the byte str with with byte\r\n\r\n and take the 2nd element
dataOnlyByte = inByteStr.split(b'\r\n\r\n')[1]
# decode the byte string of the 2nd element in to string
intoStr = dataOnlyByte.decode()
print(intoStr)
