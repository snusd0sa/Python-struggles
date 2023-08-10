student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    for (key, value) in student_dict.items():
        print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nd = {row.letter:row.code for (i, row) in nato_alphabet.iterrows()}
print(nd)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
#print(nd["M"])
result = [nd[letter] for letter in word]
print(result)