import requests

print("Hello Manu")
print("Hello World")

valid_response = requests.get("https://api.github.com")
print(valid_response.status_code)

print("Hello Manu")

name = "Manu"
print("Hello, {name}!")

user_name = "Manu"


