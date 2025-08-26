import json 
x = '{"Name": "Rafeeq","Age" : 21 , "City" : "Faridabad"}'
y = json.loads(x)
print(y['Name'])