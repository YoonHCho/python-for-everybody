''' Exercise 2:
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])

Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the
program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.
'''

'''
1. based on the code above, the code wants to print the 2nd index of a list/array. Therefore, instead of having a if statement of
if len(words) == 0 : continue , we can have a code to look if the length of words is less than 3, if len(word) < 3 : continue
since it means that it will NOT have an element at index 2 of words list/array.
'''

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
