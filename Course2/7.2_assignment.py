# _assignment.py
''' Exercise 2:
Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out 
the average spam confidence.

Test your file on the mbox.txt and mbox-short.txt files.
'''
fileName = input("Enter file name: ")
try:
    fileHandle = open(fileName)
except:
    print("File name", fileName, "doesn't exist")
    quit()

totalSum = 0.0
count = 0

for line in fileHandle:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    idx = line.find(":")
    floatNum = float(line[idx + 1:].strip())
    totalSum += floatNum
    count += 1

print("Total:", totalSum)
print("Cout:", count)
print("Average:", totalSum/count)
