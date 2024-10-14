# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#* Creating a Dictionary
# To create a dictionary we use curly brackets, {} or the dict() built-in function.
empty_dic = {}
dct = {'key1':'value1', 'key2':'value2'}

person = {
    'first_name': 'Asabeneh',
    'last_name':'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print('person:', person)
# The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

#* Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.
print('Length of person: ',len(person))

#* Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.
print(person['first_name'])
print(person['last_name'])
print(person['skills'])
print(person['skills'][0])
print(person['address']['street'])
print(person['age'])

# Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))

#* Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print('Added to person:', person)

#* Modifying Items in a Dictionary
person['first_name'] = 'Eyob'
person['age'] = 252
print('Modified first name and age:', person)

#* Checking Keys in a Dictionary
# We use the in operator to check if a key exist in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)
print('key5' in dct)

#* Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct_2 = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_2.popitem() # removes the last item
del dct['key2'] # removes key2 item

person.pop('first_name') # Removes the firstname item
person.popitem() # Removes the address item
del person['is_married'] # Removes the is_married item

#* Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('Change dictonary to list:', dct.items())

#* Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())

#* Deleting a Dictionary
# If we do not use the dictionary we can delete it completely
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#* Copy a Dictionary
# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print('Dictonary copied:', dct_copy)

#* Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print('All keys in dictonary as a list:', keys)

#* Getting Dictionary Values as a List
# The values method gives us all the values of a a dictionary as a list.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print('Values of dictonary as a list:', values)

#! 💻 Exercises: Day 8
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Maxi',
    'breed': 'German Shepherd',
    'legs': 4,
    'age': 12
}
print('Dog:', dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Boa',
    'last_name': 'Hancock',
    'gender': 'female',
    'marital_status': 'married',
    'skills': ['fighting', 'cooking', 'gardening'],
    'city': 'Island',
    'address': {
        'strret_name' : 'IslandA',
        'zipcode': '23456'
    }
}
print('student:', student)

# Get the length of the student dictionary
print('Length of student:', len(student))

# Get the value of skills and check the data type, it should be a list
print(student.get('skills'))

# Modify the skills values by adding one or two skills
student['skills'].append('painting')
print('Added new skills:', student)

# Get the dictionary keys as a list
keys = student.keys()
print('Student keys:', keys)

# Get the dictionary values as a list
values = student.values()
print('Student values:', values)

# Change the dictionary to a list of tuples using items() method
print('Change dict to list of tuples:', student.items())

# Delete one of the items in the dictionary
print('Rmoved first name: ',student.pop('first_name'))

# Delete one of the dictionaries
del student