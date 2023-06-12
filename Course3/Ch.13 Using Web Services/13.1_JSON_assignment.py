'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http: // www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http: // py4e-data.dr-chuck.net/comments_42.json(Sum=2553)
Actual data: http: // py4e-data.dr-chuck.net/comments_1792386.json(Sum ends with 33)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
    comments: [
        {
            name: "Matthias"
            count: 97
        },
        {
            name: "Geomer"
            count: 97
        }
        ...
    ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http: // py4e-data.dr-chuck.net/comments_42.json
Retrieving http: // py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("Enter 'Q' to quit OR")
    addy = input("Enter location: ")
    if len(addy) < 1 or addy == 'Q' or addy == 'q':
        break

    print('Retrieving', addy)
    response = urllib.request.urlopen(addy, context=ctx)
    data = response.read().decode()
    print(f"Retrieved {len(data)} characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if js is None:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    count = 0
    sum = 0

    for ele in js['comments']:
        count += 1
        sum += int(ele['count'])

    print(f"Count: {count}")
    print(f"Sum: {sum}")
