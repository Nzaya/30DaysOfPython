
###*------------- BOOLEAN
# Example: Boolean Values
print(True)
print(False)

###*---------- OPERATORS
#** Assignment Operators
# x = 5 # = operator
# x += 3 is x = x + 3 # += 
# x -+ 3 is x = x-3 # -=
# x *= 3 is x = x * 3 # *=
# x /= 3 is x = x / 3 # /=
# x %= 3 is x = x % 3 # %=
# x //= 3 is x = x // 3 # //=
# x **= 3 is x = x ** 3 # **=
# x &= 3 is x = x & 3 # &=
# x |= 3 is x = x | 3 # |=
# x ^= 3 is x = x ^ 3 # ^=
# x >>= 3 is x = x >> 3 # >>=
# x <<= 3 is x = x << 3 # <<=

#** Arithmetic Operators
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

#* INTEGERS
print('Addition:', 1 + 2)
print('Subtraction:', 2 - 1)
print('Multiplication:', 2 * 3)
print('Division:', 4 / 2)
print('Division without reminder:', 7 // 2)
print('Modulus:', 3 % 2)
print('Exponentiation:', 2 ** 3)

#* Example:Floats
print('Floating Point Number, PI:', 3.14)
print('Floating Point Number, gravity:', 9.81)

#* Example:Complex numbers
print('Complex number:', 1 + 1j)
print('Multiplying Complex Numbers:', (1 + 1j) * (1 - 1j))

# More examples
a = 3
b = 2

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
reminder = a % b
floor_division = a // b
exponential = a ** b

print('total', total)
print('diff', diff)
print('product', product)
print('division', division)
print('reminder', reminder)
print('floor_division', floor_division)
print('exponentiation', exponential)

#* Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2 # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

#* Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

#* Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print('N', weight)

#* Calculate the density of a liquid
mass = 75
volume = 0.075
density = mass / volume
print('density', density)

#** COMPARISON OPERATORS
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# In addition to the above comparison operator Python uses:
# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Asabeneh', 'A' in 'Asabeneh')
print('B in Asabeneh', 'B' in 'Asabeneh')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is 2 ** 2)

#* LOGICAL OPERATORS
print('3 > 2 and 4 > 3:',3 > 2 and 4 > 3)
print('3 > 2 and 4 < 3:',3 > 2 and 4 < 3)
print('3 < 2 and 4 < 3:',3 < 2 and 4 < 3)
print('True and True:', True and True)
print('3 > 2 or 4 > 3:',3 > 2 or 4 > 3)
print('3 > 2 or 4 < 3:',3 > 2 or 4 < 3)
print('3 < 2 or 4 < 3:',3 < 2 or 4 < 3)
print('True or False:', True or False)
print('not 3 > 2:',not 3 > 2)
print('not True:',not True)
print('not False:',not False)
print('not not True:',not not True)
print('not not False:',not not False)

#! 💻 Exercises - Day 3
# Declare your age as integer variable
age = 43

# Declare your height as a float variable
height = 36.0

# Declare a variable that store a complex number
complex_number = 3 + 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

base = input("Enter base:")
height = input("Enter height:")
area = 0.5 * base * height
print("area_of_triangle:", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

a = input('Enter side a:')
b = input('Enter side b:')
c = input("Enter side c:")
perimeter = a + b + c
print("perimeter_of_a_triangle:", perimeter)


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Length')
width = input('Width')

area = length * width
perimeter = 2 * (length + width)
print('Area of rectangle:', area)
print('Perimeter of rectangle:', perimeter)



# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = input("Enter radius")
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print('circle_ area:', area)
print('circle_circumference:', circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# * Slope (m)
m = 2
# * Y- intercept (b)
b = -2
# * Calculate x-intercept: set y = 0
x_intercept = -b / m

print("Slope (m):", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", b)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)


# Compare the slopes in tasks 8 and 9.


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print('on' in 'python' and 'on' in 'dragon')


# Find the length of the text python and convert the value to float and convert it to string
length = len('python')
length_as_float = float(length)
length_as_string = str(length_as_float)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# * use the modulus operator %

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division_result = 7 // 3
# Convert to interger
int_value = int(2.7)
# Check if two decimals are equal
result = floor_division_result == int_value
print(result)


# Check if type of '10' is equal to type of 10
print(type('10' == 10))

# Check if int('9.8') is equal to 10
print(type(int('9.8') == 10))


# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

hours = input("Enter hours:")
rate_per_hour = input("Enter rate per hour:")
earnings = rate_per_hour * hours
print("Your weekly earning is:", earnings)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

years_lived = int(input("Enter number of years"))
seconds_in_a_year = 365 * 24 * 60 * 60
seconds_lived = years_lived * seconds_in_a_year 
print("You have lived for {seconds_lived} seconds")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

num_rows = 5

print("Table:")
for i in range(1, num_rows + 1):
    # Claculate values of each row
    first_value = i
    second_value = 1
    third_value = first_value ** 2
    fourth_value = first_value ** 3

    print(f"{first_value} {second_value} {first_value} {third_value} {fourth_value}")