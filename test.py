#
import json

data3 = {
    
    'name': 'John Doe', 
    'age': 30,
    'city': 'New York, NY',
    'interests': ['Golf','Running','Football','Traveling'],
    'is_student': False
}

#
with open('data3.json','w') as json_file:
#
    json.dump(data3,json_file,indent=4)
#s
print("Data has been written to data3.json")
    