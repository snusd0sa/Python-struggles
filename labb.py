#def greet_with(name, location):
#    print(f"Hello {name}")
#    print(f"What is it like in {location}?") 
#
#greet_with(name="Mathias", location="Stockholm")
#

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# to use modulus here works with the courses "cheat" to add one more alphabet after the first in the list
# not a real solution imo. My solution to handle it as I did in the earlier function could also use modulus
# but would req. more code in the caesar function, but atleast it would work with other textlists....
shift = shift % 26

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the position of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-position-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

""" def encrypt(plain_text, shift_amount):
    encrypted = []
    for letter in plain_text:
        position = alphabet.index(letter)
        print(position, letter)
        if position + shift_amount > 25:
            new_letter = (position + shift_amount) - 26
        else :
            new_letter = position + shift_amount
        print (new_letter)
        encrypted.append(alphabet[new_letter])
    encrypted_string = ''.join(encrypted)
    print(encrypted_string)
 """
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#def decrypt(plain_text, shift_amount):
#    encrypted = []
#    for letter in plain_text:
#        position = alphabet.index(letter)
#        print(position, letter)
#        if position - shift_amount < 0:
#            new_letter = (position - shift_amount) + 26
#        else :
#            new_letter = position - shift_amount
#        print (new_letter)
#        encrypted.append(alphabet[new_letter])
#    encrypted_string = ''.join(encrypted)
#    print(encrypted_string)

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#if direction == "encode":
#    encrypt(text, shift)
#elif direction == "decode":
#    decrypt(text, shift)
#else:
# #   print("fel val")


def caesar(plain_text, shift_amount, direction):
    
    if direction == "decode":
        shift_amount = shift_amount * -1
    
    encrypted = []
    
    for letter in plain_text:
        position = alphabet.index(letter)
        print(position, letter)
        if position + shift_amountx > 25:
            new_letter = (position + shift_amount) - 26
        elif position - shift_amount < 0:
            new_letter = (position - shift_amount) + 26
        else :
            new_letter = position + shift_amountx
        print (new_letter)
        encrypted.append(alphabet[new_letter])
    encrypted_string = ''.join(encrypted)
    print(encrypted_string)

caesar(text, shift, direction)