def greet():
    print("Hello!")
    print("Hello Manu!")

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"Hello Welcome again {name}!")

greet_with_name("Manu")
greet()

def greet_with_fname_and_lname(last_name, first_name="Harshada"):
    print(f"Hello {first_name} {last_name}!")
#greet_with_fname_and_lname(first_name="Manu", last_name="Kumar")
#greet_with_fname_and_lname(first_name="Manu")
greet_with_fname_and_lname(last_name="Kumar")

def calculate_area(length, width):
    area = length * width
    print(f"Area  is: {area}")
calculate_area(5, 10)

def calculate_area_with_return(length, width):
    area = length * width
    return area

result = calculate_area_with_return(5, 10)
print(f"Area with return is: {result}")


discount = 10
def calculate_tax(price, tax_rate):
    tax = price * tax_rate - discount
    return tax

tax=calculate_tax(price=300, tax_rate=0.18)
print(f"Tax is: {tax}")



cgst = 0.09
def caclulate_karnataka_tax(price, sgst_rate):
    sgst = price * sgst_rate
    cgst_rate = price * cgst
    total_tax = sgst + cgst_rate
    return total_tax

karnataka_tax = caclulate_karnataka_tax(price=300, sgst_rate=0.09)
print(f"Karnataka Tax is: {karnataka_tax}")

def calculate_tamil_nadu_tax(price, sgst_rate):
    sgst = price * sgst_rate
    global cgst 
    cgst = 0.10
    cgst_rate = price * cgst
    total_tax = sgst + cgst_rate
    return total_tax

tamil_nadu_tax = calculate_tamil_nadu_tax(price=300, sgst_rate=0.18)
print(f"Tamil Nadu Tax is: {tamil_nadu_tax}")


def calculate_kerala_tax(price, tax_rate=0.18):
    tax = price * tax_rate
    return tax

kerala_tax = calculate_kerala_tax(price=300)
print(f"Kerala Tax is: {kerala_tax}")

total_tax = calculate_kerala_tax(price=300, tax_rate=0.20) + calculate_tamil_nadu_tax(price=300, sgst_rate=0.18) + caclulate_karnataka_tax(price=300, sgst_rate=0.09)
print(f"Total Tax is: {total_tax}")

tax_list = [calculate_kerala_tax(price=300), calculate_tamil_nadu_tax(price=300, sgst_rate=0.18), caclulate_karnataka_tax(price=300, sgst_rate=0.09)]
print(f"Highest Tax is: {max(tax_list)}")
print(f"Lowest Tax is: {min(tax_list)}")

def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)
