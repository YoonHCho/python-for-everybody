''' Exercise 1: 
Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called 
middle that takes a list and returns a new list that contains all but the first and last elements
'''


def chop(list):
    del list[0]
    del list[len(list) - 1]
    # OR
    # del list[-1]
    return None


def middle(list):
    # OR
    # return list[1: len(list) - 1]
    return list[1: -1]


print(chop([1, 2, 3, 4, 5]))
print(middle([1, 2, 3, 4, 5]))
