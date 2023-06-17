# From freeCodeCamp
# "32 + 698", "3801 - 2", "45 + 43", "123 + 49"
# INTO
#    32      3801      45      123\n
# + 698    -    2    + 43    +  49\n
# -----    ------    ----    -----


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    firstLine = ''
    secondLine = ''
    dashes = ''
    calculation = ''
    finalString = ''

    for ele in problems:
        firstNum, operator, secondNum = ele.split()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'"
        elif len(firstNum) > 4 or len(secondNum) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not firstNum.isdigit() or not secondNum.isdigit():
            return "Error: Numbers must only contain digits."

        maxLength = max(len(firstNum), len(secondNum)) + 2
        solved = ''
        if operator == '+':
            solved = str(int(firstNum) + int(secondNum)).rjust(maxLength)
        else:
            solved = str(int(firstNum) - int(secondNum)).rjust(maxLength)

        toAddFirstLine = firstNum.rjust(maxLength)
        toAddSecondLine = operator + ' ' + secondNum.rjust(maxLength - 2)
        dash = ''
        for _ in range(maxLength):
            dash += '-'

        if ele != problems[-1]:
            firstLine += toAddFirstLine + '    '
            secondLine += toAddSecondLine + '    '
            dashes += dash + '    '
            calculation += solved + '    '
        else:
            firstLine += toAddFirstLine + '\n'
            secondLine += toAddSecondLine + '\n'
            dashes += dash + '\n'
            calculation += solved + '\n'

    if solve:
        finalString += firstLine + secondLine + dashes + calculation
    else:
        finalString += firstLine + secondLine + dashes

    return finalString


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(
    ['3 + 855', '3801 - 2', '45 + 43', '123 + 49'], True))
print(arithmetic_arranger(
    ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
                           '888 + 40', '653 + 87']))
