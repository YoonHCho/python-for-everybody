''' Exercise 2:
Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method.
Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
'''
import re

fname = input("Enter file name: ")


def handleAverage(fname):
    try:
        fhandle = open(fname)
    except:
        print("Cannot find file name ", fname)

    numsList = [int(num) for num in re.findall(
        'New Revision: ([0-9]+)', fhandle.read())]
    print(int(sum(numsList) / len(numsList)))


handleAverage(fname)
