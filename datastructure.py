#List Data Structures
num_list = [0,1,2,3,4,5];

has_liscense = True

my_list = ["Manu", 25, True, has_liscense]

print(num_list[0])  # 0
print(num_list[1])  # 1
print(num_list[2])  # 2

print(f"My name is {my_list[0]} and I am {my_list[1]} years old. Do I have a license? {my_list[2]}")

my_list.remove(has_liscense)
my_list.append("Tata Nexon")
print(f"My name is {my_list[0]} and I am {my_list[1]} years old. Do I have a license? {my_list[2]}. I drive a {my_list[3]}.")

my_list.reverse()
new_list = my_list[0:2]
new_list = my_list[1:3]

my_list.insert(1, "K R")

for item in my_list:
    print(item)

my_list.reverse()  # This will throw an error because the list contains mixed data types (str, int, bool)
for item in range(1, 2):
    print(my_list[item])  # 4

print(my_list.index("Tata Nexon"))
print(len(my_list))
print(my_list.count("Tata Nexon"))

fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Yes, banana is in the list.")
else:
    print("No, banana is not in the list.")

fruits.sort()

if fruits:
    print("The list is not empty.")
else:
    print("The list is empty.")
# This will throw an error because the list contains mixed data types (str, int, bool)


#Dictionary Data Structures
my_dict = {}

person = {
    "name": "Manu",
    "age": 25,
    "is_adult": True
}

print(person["name"])  # Manu
print(person["age"])   # 25         
print(person["is_adult"])

person["email"] = "Manu@example.com"
person["city"] = "Bangalore"
person["age"] = 36

del person["is_adult"]
print(person.pop("email")) 
print(person.get("city"))

for item in person.values():
    print(item)
for item in person.keys():
    print(item)

while len(person.values()) > 0:
    key, value = person.popitem()
    print(f"{key}: {value}") 

my_dict = dict(Age=25, City="Bangalore")

  # True
students = {
    "manu": {"name": "Manu", "age": 35, "is_adult": True},
    "supriya": {"name": "Supriya", "age": 30, "is_adult": True},
    "Harshada": {"name": "Harshada", "age": 28, "is_adult": True}
}

for student in students.items():
    print(student[1]["name"])

#Tuple Data Structures
my_tuple = (1, 2, 3, 4, 5)

point = (3, 5)

point.count(3)  # 1
point.index(5)
print(point.index(5))
print(point[0])

colors = ("red", "green", "blue", "yellow", "purple")

print(colors[0])  # red
print(colors[1])  # green
print(colors[2])  # blue
print(colors[3])  # yellow
print(colors[4])  # purple

print(colors[-1])  # purple
single_element_tuple = (42,)
not_tuple = (42)  # This is not a tuple, it's an integer
 # Note the comma
#Sets Data Structures
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
print(my_set)

empty_set = set();
if empty_set:
    print("The set is not empty.")
else:
    print("The set is empty.")

colors = {"red", "green", "blue", "yellow", "purple"}
print("red" in colors)
print("green" in colors)
print("orange" in colors)

colors.add("orange")
colors.remove("blue")
print(colors)

scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)
print(unique_scores)

fruits = set(["apple", "banana", "orange", "banana"])
print(fruits)

  # True