# Different python data types
# variables with various data types
first_name = 'Can'     # str
city= 'Istanbul'            # str
age = 25                    # int, it is not my real age, don't worry about it

print(type('Can'))
print(type('Can') == type(first_name))
print(type(10))
print(type(0.2))
print(type(3+ 1j))
print(type(True))
print(type([1,2,3,4,5]))
print(type((1,2,3,4,5)))
print(type({'name': 'Omer', 'age': '31'}))
print(type(zip([1,2],[3,4])))

# Casting: Converting one data type to another data type.
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(float(num_str)))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

### Numbers
"""
Number data types in Python:
Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j
"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
welcome_msg = "Hello , {} {}!".format(first_name, last_name)
print(welcome_msg)