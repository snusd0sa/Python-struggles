#### Exercise 1 - squared numbers list comprehension ####
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
#Write your 1 line code 👇 below:
squared_numbers = [number ** 2 for number in numbers]
#Write your code 👆 above:
print(squared_numbers)


#### Exercise 2 - only even numbers - list comprehension ####
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
#Write your 1 line code 👇 below:
result = [number for number in numbers if number % 2 == 0]
#Write your code 👆 above:
print(result)

#### Exercise 3 - read files and only save numbers that are in both files ####
with open("file1.txt") as file1:
    file1_data = file1.readlines()
    

with open("file2.txt") as file2:
    file2_data = file2.readlines()
  

result = [int(number) for number in file1_data if number in file2_data]
print(result)

#### Exercise 4 - dictionary comprehension ####
# result = {new_key:new_value for (key, value) in dict.items() if test}
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
lista = sentence.split()
result = {word:len(word) for word in lista}
print(result)

#### Exercise 5 - dictionary comprehension with conditionals ####

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# convert to fahrenheit
# (temp_c * 9/5) + 32 = temp_f
weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)

#### Exercise 6 - dictionary comprehension with conditionals ####
# result = {new_key:new_value for (key, value) in dict.items() if test}
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# expected result: {"Angela": 56, "James": 76, "Lily": 98}
result = {student_dict["student"][i]:student_dict["score"][i] for i in range(len(student_dict["student"]))}
print(result)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)    

#### Exercise 7 - dictionary comprehension with conditionals ####
# result = {new_key:new_value for (key, value) in dict.items() if test}
#nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
#nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
#print(nato_dict)
#