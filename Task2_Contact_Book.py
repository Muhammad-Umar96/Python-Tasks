import json

print("!!Contact Book!!\n")
name = input("Enter your Name: ")
phone = input("Enter your Phone Number: ")

with open("contacts.json") as f:
    contacts = json.load(f)
        
    contacts[name] = phone

with open("contacts.json", "w")as f:
    json.dump(contacts, f, indent= 4)

    for key, value in contacts.items():
        print(f"{key} : {value}")
