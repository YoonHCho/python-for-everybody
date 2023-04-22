''' Exercise 3:
Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
Text with thelittleprince.txt
'''
import string

ltrCount = 0

fileName = input("Enter file name: ")

try:
    fhandle = open(fileName)
except:
    print(fileName, "doesn't exist")
    quit()

letters = dict()

for line in fhandle:
    # below is chaining method, first removes the punctuation and removes the digits, then lower and remove empty spaces on right
    t = tuple(line.translate(str.maketrans(
        '', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).lower().rstrip())

    for letter in t:
        # if the letter is an string and alphabet
        if isinstance(letter, str) and letter.isalpha():
            ltrCount += 1
            letters[letter] = letters.get(letter, 0) + 1

recordList = list()

for letter, count in letters.items():
    recordList.append((count, letter))

recordList.sort(reverse=True)

for count, letter in recordList:
    print(letter + ':', count, 'Frequency:', count/ltrCount)
