#
import json

#

data1 = {
    
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests':['Traveling','Football','Golf','Running','Videogames','History'], 
    'is_student': False
    
}


#Creating a Json and writing the python object contents to the json
with open('data1.json','w') as json_file:
    
    json.dump(data1,json_file,indent=4)
    
print("Data has been written to data1.json")



#
with open('data1.json','r') as json_file:
    
    #Create an object called loaded_data. Load the json file into the argument parameter.
    loaded_data = json.load(json_file)   

print("Sucessfully able to read data1.json")
print(loaded_data)



#Altering the JSON Object.
loaded_data['age'] = 34 #<-ints
loaded_data['interests'].append('Secret Hobby')


loaded_data['interests'].remove('Secret Hobby')


#Rewrite the changes to the json file. 
with open('data1.json','w') as json_file:
    
    json.dump(loaded_data,json_file,indent=4)
    
print("Data has been re-written to data1.json")



    