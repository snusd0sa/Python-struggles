# open file in write mode, need to remember to close the file!!!!!
#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close() #close the file


#use "with" keyword to open and close the file automatically
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#write to a file, default mode is "r" read mode, need to change to "w" write mode   
with open("my_file.txt", mode="w") as file: #create a new file if not exist, overwrite the file if exist
    file.write("New text.") #overwrite the file

with open("my_file2.txt", mode="a") as file: #append to the end of the file
    file.write("\nNew text with append") #append to the end of the file






