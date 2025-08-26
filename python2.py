import json
data = {
    'Name' : 'Rafeeq',
    'Rollno' : 25,
    'Cgpa' : 9.5,
    'Phone' : 9625369350,
}

jsonobj=json.dumps(data)
with open('Sample.json','w') as file:
    file.write(jsonobj)
print('Data is saver')
