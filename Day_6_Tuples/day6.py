# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). 

# Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. 

#* Methods related to tuples:
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

#* Creating a Tuple
# Empty tuple: Creating an empty tuple
empty_tuple = ()
empty_tuple = tuple #using the tuple constructor

# Tuple with initial values
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

#* Tuple length
# We use the len() method to get the length of a tuple.
tpl = ('item1', 'item2', 'item3')
len(tpl)

#* Accessing Tuple Items
#? Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print('first_item:', first_item)
print('second_item:', second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
print('first_fruit:', first_fruit)

second_fruit = fruits[1]
print('second_fruit:',second_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print('last_fruit:', last_fruit)

#? Negative indexing Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item.
tpl = ('item1', 'item2', 'item3','item4')
first_item_negative = tpl[-4]
print('first_item_negative:', first_item_negative)

second_item_negative = tpl[-3]
print('second_item_negative:', second_item_negative)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit_negative = fruits[-4]
print('first_fruit_negative:', first_fruit_negative)

second_fruit_negative = fruits[-3]
print('second_fruit_negative:', second_fruit_negative)

last_fruit_negative = fruits[-1]
print('last_fruit_negative:', last_fruit_negative)

#* Slicing tuples
# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.
#? Range of Positive Indexes
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]
print('all_items:', all_items)

all_items_1 = tpl[0:]
print('all_items_1:', all_items_1)

middle_two_items = tpl[1:3]
print('middle_two_items:', middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
print('all_fruits:', all_fruits)

all_fruits_1 = fruits[0:]
print('all_fruits_1:', all_fruits_1)

orange_mango = fruits[1:3] # doesn't include item at index 3
print('orange_mango:', orange_mango)

orange_to_the_rest = fruits[1:]
print('orange_to_the_rest:', orange_to_the_rest)

#? Range of Negative Indexes
tpl = ('item1', 'item2', 'item3','item4')
all_items_negative = tpl[-4:]
print('all_items_negative:', all_items_negative)

middle_two_items_negative = tpl[-3:-1]
print('middle_two_items_negative:', middle_two_items_negative)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits_negative = fruits[-4]
print('all_fruits_negative:', all_fruits_negative)

orange_mango_negative = fruits[-3:-1] # doesn't include item at index 3
print('orange_mango_negative:', orange_mango_negative)

orange_to_the_rest_negative = fruits[-3:]
print('orange_to_the_rest_negative:', orange_to_the_rest_negative)

#* Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruit = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print('---Fruits:', fruits)

fruits = tuple(fruits)
print(' Tuple Fruits:', fruits)

#* Checking an Item in a Tuple
# We can check if an item exists or not in a tuple using in, it returns a boolean.
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apples' in fruits)
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#* Joining Tuples
# We can join two or more tuples using + operator
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print('tpl3:', tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print('fruits_and_vegetables:', fruits_and_vegetables)

#* Deleting Tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

#! 💻 Exercises: Day 6
#? Exercises: Level 1
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Luffy', 'Roronoa', 'Chopper')
sisters = ('Namy', 'Boa', 'Robin')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print('siblings:', siblings)

# How many siblings do you have?
number = len(siblings)
print('Number of siblings:', number)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
new = list(siblings)
index = new.index('Robin')
new.insert(index + 1, 'Garp')
new.insert(index + 2, 'Bandit')

family_members = tuple(new)
print('family_members:', family_members)

#? Exercises: Level 2
# Unpack siblings and parents from family_members
unpack_siblings = family_members[0:6]
print('unapck_siblings:', unpack_siblings)

unpack_parents = family_members[6:8]
print('unpack_parents:', unpack_parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('ghee', 'milk', 'meat', 'skin')

food_stuff_tp = fruits + vegetables + animal_products
print('f00d stuffs:', food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list:', food_stuff_lt)

length = len(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index] 
print('middle_items:', middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[0:3]
print('first_three:', first_three)

last_three = food_stuff_lt[-3:]
print('last_three:', last_three)

# Delete the food_staff_tp tuple completely
del(food_stuff_tp)

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
