''' Exercise 6: 
Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when 
the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.
'''

theList = list()

while True:
    userInput = input("Enter a number: ")
    if userInput == 'done':
        break
    try:
        num = float(userInput)
    except:
        print("Please enter a number")
        continue
    theList.append(num)

print("Maximum", max(theList))
print("Minimum", min(theList))
