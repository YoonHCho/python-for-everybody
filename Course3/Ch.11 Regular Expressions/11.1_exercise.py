''' Exercise 1:
Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a
regular expression and count the number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
'''

import re

regexp = input("Please enter a regular expression: ")


def basedOnRegex(regex):
    try:
        fhandle = open("mbox.txt")
    except:
        print("Cannot find file name with mbox.txt")
        quit()

    counter = 0
    for line in fhandle:
        if re.search(regex, line):
            counter += 1
    print("mbox.txt had", counter, "lines that matched", regex)


basedOnRegex(regexp)
