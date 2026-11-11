age = 25
name = "Manu"
print(age)
print(name)
print(f"Hello, {name}!")

# Numbers data types
total = 7+8
print(total)
print(type(total))
area = 3.14 * 5 * 5
print(area)
sub = 10 - 5
print(sub)
print(type(sub))

square = 5 ** 2
print(square)
qube = 5 ** 3
print(qube)

division = 10 / 3
print(division)
floor_division = 10 // 3
print(floor_division)
modulus = 10 % 3
print(modulus)

#String data types
first_name = "Manu"
last_name = "K R"

full_name = first_name + " " + last_name
print(full_name)
print(f"Hello, {first_name} {last_name}!")


#Diffrent way to create string
name = "Manu"
hello_name = 'Hello, ' + name + '!'
print(hello_name)

#multi-line string
multi_line_string = """This is a multi-line string.
It can span multiple lines.
"""
print(multi_line_string)

#String length
first_name = "Manu"
last_name = "K R"
full_name = first_name + " " + last_name
print(len(full_name))

#String indexing
first_name = "Manu"
print(first_name[0])  # M
print(first_name[1])  # a
print(first_name[2])  # n
print(first_name[3])   # u

#String slicing
first_name = "Manu"
print(first_name[0:2])  # Ma
print(first_name[1:3])  # an
print(first_name[:3])   # Man
print(first_name[1:])   # anu       

#String methods
first_name = "Manu"
print(first_name.upper())  # MANU
print(first_name.lower())  # manu   

#String formatting
name = "Manu"
print(f"Hello, {name}!")  # Hello, Manu!    

#String concatenation
first_name = "Manu"
last_name = "K R"
full_name = first_name + " " + last_name
print(full_name)  # Manu K R    

#String interpolation
name = "Manu"
print(f"Hello, {name}!")

#String formatting with variables
user_name = "Manu"
print(f"Hello, {user_name}!")

#String Conversion
age = 25
name = "Manu"
str_age = str(age)
print(f"Hello, {str_age}!")

print(f"My name is {name} and I am {str_age} years old.")  # Hello, 25!

  # Hello, Manu!        
#Boolean data types
is_adult = True
is_child = False

#Creating a boolean variable
age = 28
can_vote = age >= 18
print(can_vote)  # True

score = 75
passed = score >= 50
print(passed)  # True