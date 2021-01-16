#Ceaser Cipher Encodinng
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_no, dire):
    e_t = ""
    for i in start_text:
        if i in alphabet:
            pos = alphabet.index(i)
            if dire == 'decode':
                e_t += alphabet[(pos-shift_no)%26]
            else:
                e_t += alphabet[(pos+shift_no)%26]
        else:
            e_t += i
        
    print(f"The {dire} text is {e_t}")   

##print(logo)   

conti = False

while not conti:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    
    inp = input("Should you want to continue? Type Yes or No ")
    
    if inp == 'No':
        conti = True
        print("Goodbye")


