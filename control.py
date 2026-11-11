temprature = 25

if temprature > 25:
    print("It's a hot day")
else:
    print("It's a cold day")

temprature = 31

if temprature > 30:
    print("It's a very hot day")
else:
    print("It's not that hot")

age = 18
has_license = False
if age >= 18 and not has_license:
    print("You can drive")
else:
    print("You cannot drive")

score = 90
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E")
else:
    print("Fail")


#Nested if statements
age = 17
has_ticket = True
if has_ticket:
    if age >= 18:
        print("You can enter the concert")
    else:
        print("You need to be at least 18 to enter the concert")
else:
    print("You need a ticket to enter the concert")