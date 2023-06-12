import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

# If error in the syntax of data, then it will give traceback error in line 16. line 16 transforms the JSON into a structured object/dictionary/list depending
# json2.py will give list
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
