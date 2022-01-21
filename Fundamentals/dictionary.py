from os import system

from requests.sessions import default_headers


#make a dictionary of (Key: Value,) items:
car_dict = {
    "model": "Mustang",
    "brand": "Ford",
    "year": 1964
}

system("cls")

print(car_dict)

print(car_dict["model"])
#or
print(car_dict.get("model"))

print(len(car_dict))

if "model" in car_dict:
    print("\nYes, 'model' is in car_dict")
else:
    print("\nNo, 'model' is not in car_dict")

#print(car_dict['default_val'])

#add definition (if key "seats" does not exist, it adds the definition to the end of the dictionary):
car_dict["seats"] = 5

#modify value:
car_dict["year"] = 2021

print(car_dict)

del car_dict["seats"]
print(car_dict)

# empty out the dictionary:
# car_dict.clear() 
#print(car_dict)

print()

#different ways to print a dictionary
for key in car_dict:
    print(key)

print()

for value in car_dict.values():
    print(value)

print()

for key, value in car_dict.items():
    print(key, ":", value)
#-------------------------------------


#Copying a dictionary
new_car_dict = car_dict.copy()


print("\n\nSorted Dictionary:")
#Sorting a dictionary
for key in sorted(car_dict):
    print(key)
    print(car_dict[key])

#---------------------------/
#nested dictionaries:::
my_family = {
    "child_1": {
        "name": "Billy",
        "birth_year": 2004
    },
    "child_2": {
        "name": "Bob",
        "birth_year": 2009
    },
    "child_3": {
        "name": "Joe",
        "birth_year": 2011   
    }
}


#to print nested dictionaries, you need to use nested for loops
print("\n\nFamily: \n---------")




for key in my_family:
    print(key) 
    #print(my_family[key])
    for subkey in my_family[key]:
        print(" ", subkey, ":", my_family[key][subkey])
  












