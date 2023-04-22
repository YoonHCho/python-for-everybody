''' Exercise 2: 
This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.

Enter a file name: mbox-short.txt
From cwen@iupui.edu Thu Jan  3 16:23:48 2008
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

try:
    fhandle = open('mbox-short.txt')
except:
    print("File doesn't exist")
    quit()

emailRecord = dict()

for line in fhandle:
    lineList = line.rstrip().split(':')
    if len(lineList) > 2 and lineList[0].startswith('From'):
        theHour = lineList[0][-2:]
        # theHourEl = lineList[0]
        # theHour = theHourEl[len(theHourEl) - 2:]
        emailRecord[theHour] = emailRecord.get(theHour, 0) + 1

hourList = list()
for hour, count in emailRecord.items():
    hourList.append((hour, count))

hourList.sort()
for h, c in hourList:
    print(h, c)
