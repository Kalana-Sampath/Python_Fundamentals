# this is subsititution cipher encryption program, basically what we are going to do is that we have a message 
# to hide a message 


import random 
import string 


chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars:  {chars}")
# print(f"key : {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text :
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")


#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text= ""

for letter in cipher_text :
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypt message: {cipher_text}")
print(f"original message: {plain_text}")

