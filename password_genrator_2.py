#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A',
          'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['!','@','#','$','%','^','&','*',')','_','+','(']

print("Welcome to pyPassword generator ")

n_l = int(input("How many letters would you like in your password?\n"))
n_s = int(input("How many symbols would you like in your password?\n"))
n_n = int(input("How many numbers would you like in your password?\n"))

st = []

x = len(letters)
y = len(num)
z = len(sym)

for i in range(0,n_l):
    st += random.choice(letters)
    

for i in range(0,n_s):
    st+= random.choice(sym)
    

for i in range(0,n_n):
    st += random.choice(num)
    
print(st)
random.shuffle(st)
print(st)

pas =""
for char in st:
    pas+=char

print(pas)    
