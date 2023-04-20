''' Exercise 4:
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

try:
    fhandle = open('mbox-short.txt')
except:
    print("Cannot find file name: mbox-short.txt")
    quit()

emailRecords = dict()

for line in fhandle:
    words = line.rstrip().split()
    if len(words) > 1 and words[0] == 'From':
        emailRecords[words[1]] = emailRecords.get(words[1], 0) + 1

maxEmail = None
maxCount = None

for email, count in emailRecords.items():
    if maxEmail is None or count > maxCount:
        maxEmail = email
        maxCount = count

print(maxEmail, maxCount)
