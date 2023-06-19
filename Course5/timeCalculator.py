'''
link: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
'''


def add_time(start, duration, day=None):
    # separate hours and minutes
    StartTime, amPm = start.split()
    amPm = amPm.upper()
    startHour, startMin = map(int, StartTime.split(':'))
    addHour, addMin = map(int, duration.split(':'))

    if amPm != 'PM' and amPm != 'AM':
        return print("Time indicator needs to be AM or PM")
    elif amPm == 'PM':
        startHour += 12
        amPm = 'AM'

    # Calculate total minutes
    totalMinutes = startMin + addMin
    extraHour = totalMinutes//60
    remainingMinutes = totalMinutes % 60

    # Calculate total hours
    totalHours = startHour + addHour + extraHour
    daysPassed = totalHours // 24
    if (totalHours % 24 >= 12):
        amPm = 'PM'
    remainingHour = totalHours % 12 or 12

    daysLater = ''
    if daysPassed == 1:
        daysLater = " (next day)"
    elif daysPassed > 1:
        daysLater = f' ({daysPassed} days later)'

    newDay = ''
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day is not None and day.lower() in [d.lower() for d in days]:
        day = day[0].upper() + day[1:].lower()
        dayIndex = (int(days.index(day)) + daysPassed) % 7
        newDay = f', {days[dayIndex]}'
    elif day is not None and day.lower() not in [d.lower() for d in days]:
        return print('Check spelling for the day')

    new_time = f'{remainingHour}:{remainingMinutes:02} {amPm}{newDay}{daysLater}'
    return print(new_time)


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
