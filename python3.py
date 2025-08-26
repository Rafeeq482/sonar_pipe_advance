import json
with open('Sample.json','r') as readfile:
    jsonobj=json.load(readfile)
print(jsonobj)