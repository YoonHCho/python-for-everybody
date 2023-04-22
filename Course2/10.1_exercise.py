''' Exercise 1: 
Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of
messages from each person using a dictionary. After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most
commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print(fname, "doesn't exist")
    quit()

record = dict()

for line in fhandle:
    lineList = line.rstrip().split()
    if len(lineList) > 2 and lineList[0] == 'From':
        record[lineList[1]] = record.get(lineList[1], 0) + 1

recordList = list()
for key, value in record.items():
    recordList.append((value, key))

recordList.sort(reverse=True)
(most, number) = recordList[0]
print(number, most)
