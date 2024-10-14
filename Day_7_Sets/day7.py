# Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

#* Creating a Set
# We use the set() built-in function.
st = set()
# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}

fruits = {'banana', 'orange', 'mango','lemon'}

#* Getting Set's Length
# We use len() method to find the length of a set.
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

fruits = {'banana', 'orange', 'mango','lemon'}
len(fruits)

#* Checking an Item
# To check if an item exist in a list we use in membership operator.
fruits = {'banana', 'orange', 'mango','lemon'}
print('mango' in fruits)

#* Adding Items to a Set
# Add one item using add()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print('fruits:', fruits)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print('Updated fruits:', fruits)

#* Removing Items from a Set
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop() # removes a random item from the set
print('Pop fruits:', fruits)

# If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print('removed_item:', removed_item)

#* Clearing Items in a Set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print('Cleared fruits:', fruits)

#* Deleting a Set
# If we want to delete the set itself we use del operator.
st = {'item1', 'item2', 'item3', 'item4'}
del st

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#* Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst) # the order is random, because sets in general are unordered
print('List to set:', st)

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits)
print('Fruits list to set:', fruits)

#* Joining Sets
# We can join two sets using the union() or update() method.
#? Union This method returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print('Union st3:', st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print('Union fruits and vegetables:',fruits.union(vegetables))

#? Update This method inserts a set into a given set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print('Update fruits:', fruits)

#* Finding Intersection Items
# Intersection returns a set of items which are in both the sets. See the example
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection = whole_numbers.intersection(even_numbers)
print('intersection:', intersection)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
similar = python.intersection(dragon)
print('Intersection 2:', similar)

#* Checking Subset and Super Set
# A set can be a subset or super set of other sets:
# Subset: issubset()
# Super set: issuperset
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
sub_set = whole_numbers.issubset(even_numbers)
print('sub_set:', sub_set)
super_set = whole_numbers.issuperset(even_numbers)
print('super_set:', super_set)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
py_dr = python.issuperset(dragon)
print('Is python superset dragon:', py_dr)

#* Checking the Difference Between Two Sets
# It returns the difference between two sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
difference = whole_numbers.difference(even_numbers)
print('difference:', difference)

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
difference_2 = python.difference(dragon)
print('difference_2:', difference_2)

#* Finding Symmetric Difference Between Two Sets
# It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
symetric_diff = whole_numbers.symmetric_difference(some_numbers)
print('symetric_diff:', symetric_diff)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
symetric_diff_2 = python.symmetric_difference(dragon)
print('symetric_diff_2:', symetric_diff_2) 

#* Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
joined = even_numbers.isdisjoint(odd_numbers) # True, because no common item
print('Is_disjoinerd? :', joined)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
joined_2 = python.isdisjoint(dragon)
print('is_disjoined_2? :', joined_2) # False, there are common items {'o', 'n'}

#! 💻 Exercises: Day 7
# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#? Exercises: Level 1
# Find the length of the set it_companies
companies_length = len(it_companies)
print('companies length:', companies_length)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('Added Twitter:', it_companies)

# Insert multiple IT companies at once to the set it_companies
more_company = ('AliExpress', 'Alibaba')
it_companies.update(more_company)
print('Added multiple companies:', it_companies)

# Remove one of the companies from the set it_companies
removed_item = it_companies.pop()
print('Removed company:', removed_item)

# What is the difference between remove and discard

# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors while discard() method doesn't raise any errors.

#? Exercises: Level 2
# Join A and B
joined = A.union(B)
print('Joined A and B:', joined)

# Find A intersection B
intersection = A.intersection(B)
print('A intersection B:', intersection)

# Is A subset of B
sub_set = A.issubset(B)
print('Is A subset of B:', sub_set)

# Are A and B disjoint sets
dis_joint = A.isdisjoint(B)
print('Are A and B disjoint sets:', dis_joint)

# Join A with B and B with A
joined_a_b = A.union(B)
print('Join A with B:', joined_a_b)

joined_b_a = B.union(A)
print('Join B with A:', joined_b_a)
# What is the symmetric difference between A and B
symetric_dif = A.symmetric_difference(B)
print('symmetric difference between A and B:', symetric_dif)

# Delete the sets completely
del it_companies
del A
del B

#? Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_ages = set(age)
print('Set ages:', set_ages)

list_length = len(age)
set_length = len(set_ages)
print(f"Set ages length is {set_length} and list length ages is {list_length}")

# Explain the difference between the following data types: string, list, tuple and set

#* String
# A string is a sequence of characters, like text. It’s immutable, meaning once created, it cannot be changed.
# Usage: For storing words, sentences, or any text data.

#* List
# A list is a collection of elements (numbers, strings, etc.). It is ordered (elements keep their position) and mutable, meaning you can modify it after creation.
# Usage: When you need a collection that can change.

#* Tuple
# A tuple is like a list, but it is immutable—once created, it cannot be changed. It is also ordered.
# Usage: When you need a collection that shouldn’t change.

#* Set
# A set is an unordered collection of unique elements. It doesn’t allow duplicate values and cannot be accessed by index because the order isn’t guaranteed.
# Usage: When you need to store unique elements and don’t care about order.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
# Split the sentence into words and convert it to a set to get unique words
unique_words =set(sentence.split())
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")