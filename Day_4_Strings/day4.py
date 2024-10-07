# Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

# * Creating a String
letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello, World'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string2 = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string2)

#* String Concatenation
first_name = "Asabeneh"
last_name = "Yetayeh"
space = ' '
full_name = first_name + space + last_name
print(full_name)
# Checking the length of a string using len() built-in function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# * Escape Sequences in Strings
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")
print('I hope everyone is enjoying the Python Challenge. \nAre you ?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backlash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

# * String formatting
# ? Old Style String Formatting (% Operator) 
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = "Asabeneh"
last_name = "Yetayeh"
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print("--formated_string--:", formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string_two = 'The area of a circle with a radius %d is %.2f.' %(radius, area)
python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formatted_string = 'The following python libraries:%s' % (python_libraries)
print("---formated_string_two---:", formated_string_two)

# ? New Style String Formatting (str.format)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string_three = 'i am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string_three)

a = 4
b = 3
print('{} + {} = {}'. format(a, b, a + b))
print('{} - {} = {}'. format(a, b, a - b))
print('{} * {} = {}'. format(a, b , a * b))
print('{} / {} = {:.2f}'. format(a, b, a/b)) # limits it to two digits after decimal
print('{} % {} = {}'. format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'. format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string_four = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string_four)

#? String Interpolation / f-Strings (Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# * Python Strings as Sequences of Characters
# Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.

#? Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# ? Accessing Characters in Strings by Index
# In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one

language = 'Python'
first_letter = language[0]
print("first_letter:", first_letter)
second_letter = language[1]
print("second_letter:",second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print("last_letter:", last_letter)

# If we want to start from right end we can use negative indexing. -1 is the last index.

language = 'Python'
last_letter = language[-1]
print("last_letter", last_letter)
second_last = language[-2]
print("second_last:", second_last)

#* Slicing Python Strings
# In python we can slice strings into substrings.

language = 'Python'
first_three = language[0:3]
print('first_three',first_three)
last_three = language[3:6]
print('last_three',last_three)
# Another way
last_three_two = language[-3:]
print('last_three_two:', last_three_two)
last_three_three = language[3:]
print('last_three_three',last_three_three)

#* Reversing a String
greeting = 'Hello, World'
print(greeting[::-1])

#* Skipping Characters While Slicing
# It is possible to skip characters while slicing by passing step argument to slice method.

language = 'Python'
pto = language[0:6:2]
print("pto:", pto)

#* String Methods
#? capitalize(): Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())

#? count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

#? endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# ? expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#? find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

#? rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))

#? format(): formats string into a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = ' I am {} {}. I am {} years old. I live in {}.'. format(first_name, last_name, age, job, country)
print("sentence:", sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The are of a circle with radius {} is {}.'.format(str(radius), str(area))
print(result)

#? index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
# print(challenge.index(sub_string, 9)) # error

#? rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))
# print(challenge.rindex(sub_string, 9)) # error

#? isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

#? isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())
num = '123'
print(num.isalpha())

#? isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal()) # False
challenge = '123'
print(challenge.isdecimal())
challenge = '\u00B2'
print(challenge.isdigit()) # False
challenge = '12 3'
print(challenge.isdecimal()) # False, space not allowed

#? isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
chalenge = '30'
print(challenge.isdigit())
challenge = '\u00B2'
print(challenge.isdigit())

#? isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric())
num = '\u00BD' # ½
print(num.isnumeric())
num = '10.5'
print(num.isnumeric())  # False

#? isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

#? islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

#? isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

#? join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print('result', result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result_a = '# '.join(web_tech)
print("result_a", result_a)

#? strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))

#? replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

#? split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))

#? title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())

#? swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

#? startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))

#! 💻 Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python'] 
sentence = ' '.join(words)

print("----sentence", sentence)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
part_1 = 'Coding'
part_2 = 'For' 
part_3 = 'All'

formattedString = '{} {} {}'.format(part_1, part_2, part_3)
print('------formattedString', formattedString)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = formattedString

# Print the variable company using print().
print('----company', company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.isupper())

# Change all the characters to lowercase letters using lower() method.
print(company.islower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
sent = formattedString

print(sent.capitalize())
print(sent.title())
print(sent.swapcase())

# Cut(slice) out the first word of Coding For All string.
first_word = formattedString[7:]
print("first_word:",first_word) 

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

# Find method
string = formattedString
result = string.find("Coding")
print(result != -1)

# In method
print("Coding" in string)

# Index method
try:
    string.index("Coding")
    print(True)
except ValueError:
    print(False)


# Replace the word coding in the string 'Coding For All' to Python.
new_string = string.replace("Coding", "Python")
print("new_string", new_string)

# Change Python for Everyone to Python for All using the replace method or other methods.
string = 'Python for Everyone'
new_string_2 = string.replace('Everyone', 'All')
print("new_string_2", new_string_2)

# Split the string 'Coding For All' using space as the separator (split()) .
split_string = company.split(" ")
print("split_string", split_string)


# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = tech_companies.split(", ")
print("split_companies", split_companies)

# What is the character at index 0 in the string Coding For All.
char = company[0]
print('--char--:', char)

# What is the last index of the string Coding For All.
chars = company[-1]
print('---chars--:', chars)

last_index = len(company) - 1
last_char = company[last_index]
print('--last_char:', last_char)

# What character is at index 10 in "Coding For All" string.
index_ten = company[10]
print('index_ten:', index_ten)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = 'Py4E'

# Create an acronym or an abbreviation for the name 'Coding For All'.
acronym_1 = 'Co4A'

# Use index to determine the position of the first occurrence of C in Coding For All.
position_C = company.index('C')
print('position of the first occurrence of C:', position_C)

# Use index to determine the position of the first occurrence of F in Coding For All.
text_F = company.index('F')
print('position of the first occurrence of F', text_F)

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = 'Coding For All People'
text_l = text.rfind('l')
print('last occurrence of l:', text_l)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
positionA = sentence.index('because')
print("first occurrence of the word 'because':",positionA)

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
positionB = sentence.rfind('because')
print('position of the last occurrence of the word because :', positionB)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because because because')
end_index = start_index + len('because because because')
phrase = sentence[start_index:end_index]
print("Slicing out the phrase 'because because because':", phrase)

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurence = sentence.find('because')
print("first occurrence of the word 'because':", first_occurence)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
s_index = sentence.find('because because because')
e_index = s_index + len('because because because')
phrase_1 = sentence[s_index:e_index]
print("Slicing out the phrase 'because because because':", phrase_1)

# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      ' 
cleaned_text = text.strip()
print('cleaned_text:', cleaned_text)

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
clen = '30DaysOfPython'
print(clen.isidentifier())

# thirty_days_of_python
clean_1 = 'thirty_days_of_python'
print(clean_1.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
words = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
final =  '# '.join(words)
print('final:', final)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
format = 'The area of a circle with radius {} is {}'.format(radius, area)
print('---format---:', format)

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))