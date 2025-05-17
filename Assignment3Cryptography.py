import math
import sys
import time

# Create a list of uppercase and lowercase ASCII letters
alpha_up = [chr(i) for i in range(65, 91)] 
alpha_low = [chr(i) for i in range(97, 123)]

#create list containing files
data = []
# List of filenames in the folder 
filenames = [
    'message0 (1).txt',
    'message1 (1).txt',
    'message2 (1).txt',
    'message3 (1).txt',
    'message4 (1).txt',
]

y = 3

for n in filenames:
    if n != "keys":
        with open(f'C:\\Users\\sebas\\Python\\data\\{n}', 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line)

key_imp = []

with open(f'C:\\Users\\sebas\\Python\\data\\keys (1).txt')as file:
    for line in file:
        key_imp.append(line.strip("\n"))
# print(data, key_imp)

mes = data[y]
keyword = key_imp[y]
Choice = input("Decrypt or Encrypt? [D/E]")

#storing inputs
key_char = list(keyword)
mes_char = list(mes) 
print(key_char, mes_char)

#storing results of shifts
new_mes = [] 

# map all letter of the alphabet to a list with numbers starting at 1 
def wrap_keyword():
    K_new = []  # will hold the repeated keyword
    j = 0
    for i in range(len(mes_char)):  # loop over every character in the message
        # Use modulo to wrap keyword characters
            if mes_char[i].isalpha():
                K_new.append(key_char[j % len(key_char)])
                j += 1
            else:
                K_new.append(mes_char[i])
    return K_new

# Get the repeated/wrapped keyword list - need to call the defined function
K_new = wrap_keyword()

    
#if they choose to encrypt their message, run this
if Choice.upper() == "E":
    for i in range(len(mes_char)):
        m = mes_char[i]
        k = K_new[i]
        try:
            if m.isupper():
                # Convert A-Z to 0–25 range using ord('A') = 65
                shift = ord(k.upper()) - ord('A') # this is the difference in the ASCII number (the actual quantity of spaces shifted)
                shifted = (ord(m) - ord('A') + shift) % 26 #now shifting them and wrapping them for when they exceed the ALPHABETICAL RANGE (NOT ASCII YET) - LEMON -> LEMONLEM, once it goes over 26, it will automatically go back to first "m" and shift it. 
                new_char = chr(shifted + ord('A')) #now storing the shifted values with regards to the ASCII RANGE
                new_mes.append(new_char) #putting that new shifted word into a list

            elif m.islower():
                # Convert a-z to 0–25 range using ord('a') = 97
                shift = ord(k.lower()) - ord('a')
                shifted = (ord(m) - ord('a') + shift) % 26
                new_char = chr(shifted + ord('a'))
                new_mes.append(new_char)
                    
            else:
                
                new_mes.append(m)#if the input contains characters that are not letters, they will remain in the same spot in the new list
        except Exception as e:
            print(f'Your input gave this error: {e}')
            
#if they choose to decrypt their message, use this:                   
elif Choice.upper() == "D":
    for i in range(len(mes_char)):
        m = mes_char[i]
        k = K_new[i]
        try:
            if m.isupper():
                # Convert A-Z to 0–25 range using ord('A') = 65
                shift = ord(k.upper()) - ord('A') # this is the difference in the ASCII number (the actual quantity of spaces shifted)
                shifted = (ord(m) - ord('A') - shift) % 26 #now shifting them and wrapping them for when they exceed the ALPHABETICAL RANGE (NOT ASCII YET) - LEMON -> LEMONLEM, once it goes over 26, it will automatically go back to first "m" and shift it. 
                new_char = chr(shifted + ord('A')) #now storing the shifted values with regards to the ASCII RANGE
                new_mes.append(new_char) #putting that new shifted word into a list

            elif m.islower():
                # Convert a-z to 0–25 range using ord('a') = 97
                shift = ord(k.lower()) - ord('a')
                shifted = (ord(m) - ord('a') - shift) % 26
                new_char = chr(shifted + ord('a'))
                new_mes.append(new_char)
                    
            else:
                
                new_mes.append(m)#if the input contains characters that are not letters, they will remain in the same spot in the new list
        except Exception as e:
            print(f'Your input gave this error: {e}')
                  
else:
    print("Invalid choice. Please enter 'D' to Decrypt or 'E' to Encrypt.")
    sys.exit(1)       
     
#print output of encryption or decryption

print(''.join(new_mes))

# i think problem is that 26%26 = 0, and that means that for every character that gets shifted to position 26, it dissapears, which might be why my code is slightly off. make sure you understand why this doesnt work. 