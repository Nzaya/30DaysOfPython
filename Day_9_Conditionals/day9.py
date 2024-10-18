# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:
# Conditional execution: a block of one or more statements will be executed if a certain expression is true
# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover if, else, elif statements. The comparison and logical operators we learned in previous sections will be useful here.

#* If Condition
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.
a = 3
if a > 0:
    print('A is a positive number')

#* If Else
# If condition is true the first block will be executed, if not the else condition will run.
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#* If Elif Else
# In our daily life, we make decisions on daily basis. We make decisions not by checking one or two conditions but multiple conditions. As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#* Short Hand
a = 3
print('A is posiive') if a > 0 else print('A  is negative')

#* Nested Conditions
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# We can avoid writing nested condition by using logical operator and.
#* If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive interger')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

#* If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied!')


#! 💻 Exercises: Day 9
#? Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

user_input = int(input('Enter your age:'))
age_diff = 18 - user_input

if user_input > 18:
    print('You are old enough to drive')
else:
    print(f"You need {age_diff} more years to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

your_age = int(input('Enyer your age:'))
my_age = 22

if my_age > your_age:
    age_diff = my_age - your_age
    if my_age - your_age == 1:
        print(f"You are {age_diff} year younger than me")
    else:        
        print(f"You are {age_diff} years younger than me")
elif your_age > my_age:
    age_diff = your_age - my_age
    if your_age - my_age == 1:
        print(f"You are {age_diff} year older than me")
    else:
        print(f"You are {age_diff} years older than me.") 


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

num_1 = int(input('Enter number one:'))
num_2 = int(input('Enter number two:'))

if num_1 < num_2:
    print(f"{num_1} is less than {num_2}")
elif num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
else:
    print(f"{num_1} is equal to {num_2}")

#? Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

grade = 40
if grade >= 90 and grade <= 100:
    print('90 -100, A')
elif grade >= 70 and grade <=89:
    print('70 - 89, B')
elif grade >= 60 and grade <= 69:
    print('60 - 69, C')
elif grade >= 50 and grade <=59:
    print('50 - 59, D')
else:
    print('0 - 49, F')


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input('Enter month of the year:')
if month in ['September','October','November']:
    print('The season is Autumn')
elif month in ['December', 'January' , 'February']:
    print('The season is Winter')
elif month in ['March', 'April' , 'May']:
    print('The season is Spring')
elif month in ['June', 'July', 'August']:
    print('The season is Summer')
else:
    print('Invalid month entered')


# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = 'apple'

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print('fruits:', fruits)

#? Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    skills = person['skills']
    middle_index = len('skills') // 2
    middle_skill = skills[middle_index]
    print(f"The middle skill is: {middle_skill}")
else:
    print('No skill found')
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
    skills = person['skills']
    print('Python' in skills)
else:
    print('Python is not among the skills')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print('He is a backend developer')
    elif ('React','Node','MongoDB').issubset(skills):
        print('He is a fullstack developer')
    else:
        print('Unknown title')
else:
    print('No skills data available')

# If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred'] == True:
    f_name = person['first_name']
    l_name = person['last_name']
    country = person['country']
    print(f"{f_name} {l_name} lives in {country}. He is married")
else:
    print('He is not married')

