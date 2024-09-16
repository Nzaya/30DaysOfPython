# Some of the most commonly used Python built-in functions are the following: print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir(). 

###*--------------- VARIABLES
# Python Variable Name Rules
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

# Here are some example of valid variable names:
# firstname
# lastname
# age
# country
# city
# first_name
# last_name
# capital_city
# _if # if we want to use reserved word as a variable
# year_2021
# year2021
# current_year_2021
# birth_year
# num1
# num2

#* Variables in python
import math


first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = {'HTML', 'CSS', 'JS', 'React', 'Python'}
person_info = {
    'firstName': 'Asabeneh',
    'lastName': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

#* Printing the values stored in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last Name', last_name)
print('Last name length:', len(last_name))
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Person Information:', person_info)


#* Declaring Multiple Variable in a Line
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsinki', 250, True

print("----Multiple Declaration----",first_name, last_name, country, age, is_married)

#* Getting user input using the input() built-in function
first_name = input('What is your first name:')
age = input('How old are you?')

print(first_name)
print(age)

###*--------------- DATA TYPES
# Checking Data types and Casting
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':'yes'}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))   #zip

#* Casting: 
# Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. 

# int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = '10.6'
# print('num_int', int(num_str))
print('num_float', float(num_str))

# str to list
first_name = 'Asabeneh'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)

#* Numbers
# Number data types in Python:
# Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
# Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

#!💻 Exercises - Day 2
#? Exercises: Level 1
# Declare a first name variable and assign a value to it
first_name ='Judas'
# Declare a last name variable and assign a value to it
last_name = 'Iscariot'
# Declare a full name variable and assign a value to it
full_name = first_name  + ' ' + last_name
print("Full Name:",full_name)
# Declare a country variable and assign a value to it
country = 'Kenya'
# Declare a city variable and assign a value to it
city = 'Nairobi'
# Declare an age variable and assign a value to it
age = 30
# Declare a year variable and assign a value to it
year = 1999
# Declare a variable is_married and assign a value to it
is_married = True
# Declare a variable is_true and assign a value to it
is_true = 'yes'
# Declare a variable is_light_on and assign a value to it
is_light_on = 'no'
# Declare multiple variable on one line
first_name, last_name, is_married, is_light_on, is_true = 'Judas', 'Iscariot', True, 'yes', 'no' 

print('------------Multiple Variable:', first_name, last_name, is_married, is_light_on, is_true)

#? Exercises: Level 2
# Check the data type of all your variables using type() built-in function

# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
f1 = len(first_name)
l1 = len(last_name)
print(f1 - l1) 
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30
area = math.pi * r * r
print('area', area)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
radius = float(input('Enter radius'))
circum_of_circle = 2 * math.pi * radius
print("circumference:", circum_of_circle)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter first name")
last_name = input("Enter last name")
country = input("Enter a country")
age = input("Enter age")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
