numbers = [1, 2, 3]

# list comprehension,  [key]
# new_list = ["new_item" for "n" in "list"]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Mathias"
new_list = [letter for letter in name]
print(new_list)

 
new_list = [n * 2 for n in range(1, 5)]
print(new_list)

# conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)





