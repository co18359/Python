from IPython.display import clear_output
import random
from hangman_art import logo,stages
from hangman_word import word_list


x = random.choice(word_list)
#print(x)
print(logo)

l = len(x)

dis = []        

for i in range(0,l):
    dis += ['_'] 

lives = 6
    
e_o_g = False
d = ''
while not e_o_g:
    wo  = input("Guess a word?").lower()
    clear_output(wait=True)
    if wo==d:
        print("You have already choosen this. Please choose another")
    for i in range(l):
        p = x[i]
        if p==wo:
            dis[i]= wo
            d = wo
    if wo not in x:
        lives -= 1
        print("You have choosen the wrong word and you have lost one life ")
    if lives ==0:
        e_o_g = True
        print("You loose")
        
    if "_" not in dis:
        e_o_g = True
        print("You win")
    print(dis)
    
    print(stages[lives])
    
              
             
    
            
    
    
    
     
        
    

