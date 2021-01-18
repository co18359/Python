import random
from IPython.display import clear_output



def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def cal_score(x):
    p=0
    if sum(x)==21 and len(x)==2:
        return 0
    if 11 in x and sum(x)>21:
        x.remove(11)
        x.append(1)
    for i in x:
        p+=i
    return p


def play():
    
    def compare(usc, compc):
        if usc==compc:
            return "Draw :)"
        elif compc == 0:
            return "Lose, opponent has black jack :("
        elif usc==0:
            return "You win :)"
        elif usc>21:
            return "You Lose, you went over :("
        elif compc>21:
            return "You win,opponent you went over :)"
        elif usc>compc:
            return "You win:)"
        else:
            return "You loose:("
     
    user = []
    comp = []
    for i in range(2):
        user.append(deal_card())
        comp.append(deal_card())

    
    over = False
    while not over:
        usc = cal_score(user)
        compc = cal_score(comp)

        print(f"Your cards {user}: Current score: {usc} ")
        print(f"Computers card {comp[0]}")

        if usc == 0 or compc ==0 or usc>21:
            over = True

        else:
            ask = input("Type 'y' to get another ,or 'n' to pass ")
            if ask == "y":
                user.append(deal_card())
            else:
                over = True
    
    while compc!=0 and compc < 17:
        comp.append(deal_card())
        compc = cal_score(comp)

    print(f"Your cards {user}: Current score: {usc} ")
    print(f"Computers cards {comp}: Score: {compc}")
    print(compare(usc,compc))
    


while input("Do you want to play game of blackjack Type 'y' or 'n'? ")=='y':
    play()
    
