''' Exercise 5:
This program records the domain name (instead of the address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''

try:
    fhandle = open('mbox-short.txt')
except:
    print("Cannot find file name: mbox-short.txt")
    quit()

record = dict()

for line in fhandle:
    line = line.rstrip().split()
    if len(line) > 1 and line[0] == 'From':
        email = line[1]
        index = email.find('@')
        domainName = email[index + 1:]
        record[domainName] = record.get(domainName, 0) + 1

print(record)
