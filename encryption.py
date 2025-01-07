import random 
import string

char = " "+string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)
#print(f"char{char}")
#print(f"key{key}")

# asking for the input from the user

user_input = input("Enter the thing that you want to encrypt : ")
encry_text = ""

for letter in user_input:
    ind  = char.index(letter)  #index take the index of letter 
    encry_text += key[ind]     #then key[ind] is key is random list of char 

print(f"The original text :{user_input}")
print(f"The encrypted text :{encry_text}")

#Decryption 
user_input = input("Enter the thing that you want to decrypt : ")
decry_text = ""

for letter in user_input:
    ind  = key.index(letter)  #index take the index of letter 
    decry_text += char[ind]     #then key[ind] is key is random list of char 

print(f"The original text :{user_input}")
print(f"The encrypted text :{decry_text}")
