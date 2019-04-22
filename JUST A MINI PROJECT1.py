#BY_KRISH_RAWAT

import random
def name_to_number(name):
    if name=="Rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="Paper":
        return 2
    elif name=="Pizard":
        return 3
    elif name=="Scissors":
        return 4
    else:
        print("invalid input")


def number_to_name(number):
    if number==0:
        return "Rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "Paper"
    elif number==3:
        return "Lizard"
    elif number==4:
        return "Scissors"
    else:
        print("invalid input")
    

def rpsls(player_choice):     
    print ("")
    print ("Player chooses " + player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print ("Computer chooses " + comp_choice)

    x=(comp_number-player_number)%5
    if x==0:
        print ("Player and computer tie!")
    elif 0<x<=2:
        print ("Computer wins!")
    else:
        print ("Player wins!")
    
x=rpsls(input().title())

