''' Exercise 1:
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
'''

index = None


def reverseStr(str):
    index = len(str) - 1
    while index >= 0:
        print(str[index])
        index -= 1
    print("finished")


reverseStr('Hello World')


################
''' Exercise 2:
Given that fruit is a string, what does fruit[:] mean?
'''

# fruit[:] will print the whole string. [:] is a slice method, both left side and right side of : will be a number of an index
# The left number of : will be the starting point of the element, inclusive.
# The right number of : will be the end point, exclusive. if no number is present like in the example, will be the whole string

fruit = "apple"
print(fruit[:])


################
''' Exercise 3:
word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)

Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
'''


def count(str, char):
    count = 0
    for letter in str:
        if letter == char:
            count += 1
    return count


print(count("banana", 'a'))


################
''' Exercise 4:
There is a string method called count that is similar to the function in the previous exercise.
Write an invocation that counts the number of times the letter a occurs in “banana”.

https://docs.python.org/library/stdtypes.html#string-methods
'''

print('Ex 5:', 'banana'.count('a'))
