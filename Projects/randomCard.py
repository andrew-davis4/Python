class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from ast import match_case
from random import randrange
from os import system

def card(value, suit):
    Card = ""
    match value:
        case 1:
            Card += "A"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card      
        case 2:
            Card += "2"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 3:
            Card += "3"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 4:
            Card += "4"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 5:
            Card += "5"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 6:
            Card += "6"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 7:
            Card += "7"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 8:
            Card += "8"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 9:
            Card += "9"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 10:
            Card += "10"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 11:
            Card += "J"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 12:
            Card += "Q"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case 13:
            Card += "K"
            match suit:
                case 1:
                    Card += "♧"
                case 2:
                    Card += "♡"
                case 3: 
                    Card += "◇"
                case 4:
                    Card += "♤"
            return Card  
        case _:
            return Card

print("\033[2;32;44m Welcome to guess the card game!\n")
	
print("\033[1;32;40m Green\033[1;37;40m")


cardNumber = randrange(13)+1
cardSuit = randrange(4)+1

# system("cls")
print("Card: ",card(cardNumber, cardSuit))

coin = randrange(2)+1

if coin == 1:
    print("Coin: tails")
else:
    print("Coin: heads")




