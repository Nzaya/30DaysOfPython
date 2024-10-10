# There are four collection data types in Python :
# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

#* How to Create a List
# Using list built-in function
lst = list()
empty_list = list()
print(len(empty_list))

# Using square brackets, []
lst = []
empty_lst = []
print(len(empty_lst))

# Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal Products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web Technologies:', web_techs)
print('Number of web technologies', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]

#* Accessing List Items Using Positive Indexing
first_fruit = fruits[0]
print('first_fruit', first_fruit)
second_fruit = fruits[1]
print('second_fruit', second_fruit)
last_fruit = fruits[3]
print('last_fruit', last_fruit)
# last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print('last_fruit', last_fruit)

#* Accessing List Items Using Negative Indexing
fir_fruit = fruits[-4]
print('first_fruit_negativeIndexing:', fir_fruit)
las_fruit = fruits[-1]
print('last_fruit_negativeIndexing:', las_fruit)
sec_last = fruits[-2]
print('secondLast_fruit_negativeIndexing:', sec_last)

#* Unpacking List Items
list_1 = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list_1
print('first_item:', first_item)
print('second_item:', second_item)
print('third_item:', third_item)
print('rest', rest)

first_fruit, second_fruit, third_fruit, *rest = fruits
print('first_fruit', first_fruit)
print('second_fruit', second_fruit)
print('third_fruit', third_fruit)
print('rest',rest)

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print('first', first)
print('second', second)
print('third', third)
print('rest', rest)
print('tenth', tenth)

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print('gr:', gr)
print('fr:', fr)
print('bg:', bg)
print('sw:', sw)
print('scandic:', scandic)
print('es:', es)

#* Slicing Items from a List
# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
all_fruits = fruits[0:4] # it returns all the fruits
all_fruits_1 = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]  # here we used a 3rd argument, step. It will take every 2cnd item

print('all_fruits:', all_fruits)
print('all_fruits_1:', all_fruits_1)
print('orange_and_mango:', orange_and_mango)
print('orange_mango_lemon:', orange_mango_lemon)
print('orange_and_lemon:', orange_and_lemon)

# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
all_fruits_negative = fruits[-4:] # it returns all the fruits
orange_and_mango_negative = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon_negative = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order

print('all_fruits_negative:', all_fruits_negative)
print('orange_and_mango_negative:', orange_and_mango_negative)
print('orange_mango_lemon_negative:', orange_mango_lemon_negative)
print('reverse_fruits:', reverse_fruits)

#* Modifying Lists
# List is a mutable or modifiable ordered collection of items.
fruits[0] = 'avocado'
print('---Fruits--:', fruits)

fruits[1] = 'apple'
print('----fruits---:', fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print('---fruits:', fruits)

#* Checking Items in a List
# Checking an item if it is a member of a list using in operator
does_exist = 'banana' in fruits
print('does_exist:', does_exist)
does_exist_1 = 'lime' in fruits
print('does_exist_1:', does_exist_1)

#* Adding Items to a List
# To add item to the end of an existing list we use the method append().
fruits.append('apple')
print('---Add apple--:', fruits)
fruits.append('lime')
print('--Add lime--:', fruits)

#* Inserting Items into a List
# We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() methods takes two arguments:index and an item to insert.
fruits.insert(2, 'apple') # insert apple between orange and mango
print('---Inserting apple between orange and mango---:', fruits)
fruits.insert(3, 'lime')
print('---Inserting lime---:', fruits)

#* Removing Items from a List
# The remove method removes a specified item from a list
fruits.remove('avocado')
print('Remove avocado:', fruits)
fruits.remove('apple')
print('Remove apple:', fruits)

#* Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits.pop()
print('Pop fruits:', fruits)

fruits.pop(0)
print('Pop fruits index 0:', fruits)

#* Removing Items Using Del
del fruits[0]
print('Delete fruit at index 0:', fruits)
del fruits[1]
print('Delete fruit at index 1:', fruits)
del fruits[1:3]
print('this deletes items between given indexes:', fruits)
del fruits # This should give: NameError: name 'fruits' is not defined
# print(fruits)

#* Clearing List Items
# The clear() method empties the list:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print('Clearing fruits:', fruits)

#* Copying a List
# It is possible to copy a list by reassigning it to a new variable in the following way: list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print('Fruits Copy:', fruits_copy)

#* Joining Lists
# Plus Operator (+)
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print('Integers:', integers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print('fruits_and_vegetables:', fruits_and_vegetables)

# Joining using extend() method The extend() method allows to append list in a list. See the example below.
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Negative_numbers:', negative_numbers)
fruits.extend(vegetables)
print('Extend; Fruits and vegetables:', fruits)

#* Counting Items in a List
# The count() method returns the number of times an item appears in a list:
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

#* Finding Index of an Item
# The index() method returns the index of an item in the list:
print(fruits.index('orange'))
print(ages.index(24))

#* Reversing a List
# The reverse() method reverses the order of a list.
fruits.reverse()
print('Reverse fruits:', fruits)
ages.reverse()
print('Reverse ages:', ages)

#* Sorting List Items
# To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

# sort(): this method modifies the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print('Sort fruits:', fruits)

fruits.sort(reverse=True)
print('Reverse fruits:', fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print('Sort ages:', ages)

ages.sort(reverse=True)
print('Reverse Ages:', ages)

# sorted(): returns the ordered list without modifying the original list
print(sorted(fruits))
fruits = sorted(fruits,reverse=True)
print('Reverse sorted fruits:', fruits)


#! 💻 Exercises: Day 5
#? Exercises: Level 1
# Declare an empty list
list = []
print('Empty list:', list)

# Declare a list with more than 5 items
list = ['name', 'age', 'country', 'city', 'phone_number', 'continent']
print('list with more than 5 items:', list)

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
# Get the first item
print('First item:',list[0])

# Get the last item
last_index = len(list) - 1
last_item = list[last_index]
print('Last Item:', last_item)
print('Last thing:', list[-1])

# Get the middle item
middle_index = len(list) // 2 
# For an even number of elements, get both middle elements
middle_items = list[middle_index - 1:middle_index + 1]
print('Middle Items:', middle_items)


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Barbie', 22, '130cm', 'single', {'address': '123 Saumu Port'}]
print('mixed_data_types:', mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print('IT Companies:', it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
# First
print('First company is:', it_companies[0])

# Middle
middle_index = len(it_companies) // 2
middle_items = it_companies[middle_index]
print('Middle company:', middle_items)

# Last
print('Last company:', it_companies[-1])

# Print the list after modifying one of the companies
it_companies.pop(0)
print('Pop company:', it_companies)

# Add an IT company to it_companies
it_companies.insert(2,'AliExpress')
print('Insert company:', it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Facebook')
print('Insert Facebook in middle:', it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print("to uppercase:", it_companies)

# Join the it_companies with a string '#;  '
joint_companies = '# '.join(it_companies)
print('joint_companies:', joint_companies)

# Check if a certain company exists in the it_companies list.
company = 'Facebook'
check = company in it_companies
print('Check if a certain company exists:', check)

# Sort the list using sort() method
it_companies.sort()
print('Companies sorted:',it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print('Reveresed list:', it_companies)

# Slice out the first 3 companies from the list
companies = it_companies[3:]
print('Slicing out the first 3 companies:', companies)

# Slice out the last 3 companies from the list
company = it_companies[-3:]
print('Slicing out the last 3 companies', company) 

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
print('Slicing out the middle company:', middle_company) 

# Remove the first IT company from the list
# using pop
list = it_companies.pop(0)
print('Removed company:', list)

# using del
del it_companies[0]
print('Removed also company:', it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) //2
middle_company = it_companies[middle_index]
print('Middle company is:', middle_company)

# Remove the last IT company from the list
del it_companies[:-1]
print('Remove the last IT company:', it_companies)

# Remove all IT companies from the list
it_companies.clear()
print('Remove all IT companies:', it_companies)

# Destroy the IT companies list
del it_companies
# print('Destroyed the IT companies list:', it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end
print('joined_list:', joined_list)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
print('Full Stack:', full_stack)

index = full_stack.index('Redux')
full_stack.insert(index + 1, 'Python')
full_stack.insert(index + 2, 'SQL')

# it_companies[index + 1:index + 1] = ['Python', 'SQL']

print('Insert to full stack:', full_stack)

#? Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# sort
ages.sort()
print('Sorted ages:', ages)

#min Age
min_age = min(ages)
print('Min Age:', min_age)

# max Age
max_age = max(ages)
print('Max age:', max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print('Instert to ages:', ages)

# Find the median age (one middle item or two middle items divided by two)
# sort first
ages.sort()
# calc median
n = len(ages)
if n % 2 == 1 : #Odd number of items
    median = ages[n // 2]
else: #Even number of items
    middle1 = ages[n // 2 - 1]
    middle2 = ages[n // 2]
    median = (middle1 + middle2) / 2

print("Median age:", median)

# Find the average age (sum of all items divided by their number )
ages.sort()

n = len(ages)
total_sum = sum(ages)

average = total_sum / n
print('Average of ages is:', average)

# Find the range of the ages (max minus min)
ages.sort()

max_age = max(ages)
min_age = min(ages)

age_range = max_age - min_age
print('Range is:', age_range)
# Compare the value of (min - average) and (max - average), use abs() method
# Calc the diff
min_diff = min_age - average
max_diff = max_age - average

# Calc absolute values
abs_min_diff = abs(min_diff)
abs_max_diff = abs(max_diff)

# Print the values for reference
print(f"Min Age: {min_age}, Max Age: {max_age}, Average Age: {average:.2f}")
print(f"Absolute difference from min: {abs_max_diff:.2f}, Absolute difference form max: {abs_max_diff:.2f}")

# Compare absolute values
if abs_min_diff > abs_max_diff:
    print("The absolute difference from the minimum age is greater than that from the maximum age.")
elif abs_min_diff < abs_max_diff:
    print("The absolute difference from the maximum age is greater than that from the minimum age.")
else:
    print("The absolute differences from both minimum and maximum ages are equal.")

# Find the middle country(ies) in the countries list
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'];

middle_index = len(countries) // 2
middle_countries = countries[middle_index -1:middle_index + 1]
print('Midddle country:', middle_countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# Calc length
n = len(countries)

if n % 2 == 0:
    middle_index = n // 2 #For even length
else:
    middle_index = (n // 2) + 1  #For odd length

#Divide list into two
first_half = countries[:middle_index] # Slicing from start to middle
second_half = countries[middle_index] # Slicing from middle to end

print('First half countries:', first_half)
print('Second half countries:', second_half)

#Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_country, second_country, third_country, *scandic_countries = countries
print('First Country:', first_country)
print('Second Country:', second_country)
print('Third Country:', third_country)
print('Scandic Country:', scandic_countries)