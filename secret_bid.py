#Secret Bid
from IPython.display import clear_output

def find_hig(dic):
    hb = 0
    winner = ""
    for i in dic:
        ba = dic[i]
        if ba>hb:
            hb = ba
            winner = i
    print(f"The winner is {winner} with bid amaount {hb} ")

aa = False
dic = {}
while not aa:
    name = input("Enter yout name? ")
    price = int(input("Enter your bid price? "))
    dic[name] = price
    ask = input("Can you see any other bidder in room? Type yes or no? ").lower()            
    if ask=='no':
        aa = True
        find_hig(dic)
    elif ask=='yes':
        clear_output(wait=True)
                     
#print(dic)

        


