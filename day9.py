import os
from art import logo
print(logo)

programming_dictionary = {"Bug": "An error in a program that....",
                          "Function": "A piece of code that yoiu cna easiliy...",
                          "Loop": "The action of doing something over and over again."}

print(programming_dictionary["Bug"])

#Adding new items to dict

programming_dictionary["Test"] = "The blaha blaha habla"

print(programming_dictionary)

# empty_dictionary = {}
# also wipes an existing dict.  ex. programming_dictionary{} would clear it

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])







#os.system('cls')