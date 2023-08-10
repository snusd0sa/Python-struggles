#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
print(letter)

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines() # returns a list of strings with \n at the end
    print(names)
stripped_names = [names.strip() for names in names]
print(stripped_names)

for name in stripped_names:
    new_letter = letter.replace("[name]", name)
    print(new_letter)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(new_letter)
