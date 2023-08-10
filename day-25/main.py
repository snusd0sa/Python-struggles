
# read lines from a file and put in a list
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# strip the \n from the end of each line
# stripped_data = [line.strip() for line in data]
# print(stripped_data)


import csv


# complicated way , use pandas instead

with open("weather_data.csv") as file:
    data = csv.reader(file)    
    temperatures = []
    for row in data: # each row is a list
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
    
# easier way
import pandas
data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))
data_list = data["temp"].to_list()
print(data_list)
print(type(data_list))
average = sum(data_list) / len(data_list)
print(average)
print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition) # same as above

print(data[data.day == "Monday"]) # get row where day is Monday
print(data[data.temp == data.temp.max()]) # get row where temp is max
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9 / 5 + 32) # convert to fahrenheit

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
    }
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")