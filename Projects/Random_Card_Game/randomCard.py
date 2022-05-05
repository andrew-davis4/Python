class textColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from random import randrange as rr
from os import system
import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

def testColours():
    system("cls")
    s = "\n\n{}HEADER\n{}OKBLUE\n{}OKCYAN\n{}OKGREEN\n{}WARNING\n{}FAIL\n{}ENDC\n{}BOLD\n{}UNDERLINE{}\n".format(textColours.HEADER, textColours.OKBLUE, textColours.OKCYAN, textColours.OKGREEN, textColours.WARNING, textColours.FAIL, textColours.ENDC, textColours.BOLD, textColours.UNDERLINE, textColours.ENDC)

    return s
def card(value, suit):
    Card = ""
    match value:
        case 1:
            Card += "A"  
        case 2:
            Card += "2"
        case 3:
            Card += "3"
        case 4:
            Card += "4"
        case 5:
            Card += "5"
        case 6:
            Card += "6"
        case 7:
            Card += "7" 
        case 8:
            Card += "8"
        case 9:
            Card += "9"
        case 10:
            Card += "10"
        case 11:
            Card += "J" 
        case 12:
            Card += "Q"  
        case 13:
            Card += "K"
        case _:
            Card += "{}This method was called on incorrectly".format(textColours.FAIL)
    match suit:
        case 1:
            Card += "♧"
        case 2:
            Card += "♡"
        case 3: 
            Card += "◇"
        case 4:
            Card += "♤"
        case _:
            return Card
    return Card
def pickCard():
    print("\nCard: ", card((rr(13)+1), (rr(4)+1)))
def coin():
    return rr(2)+1
def coinOrCard():
    goAgain = True

    while goAgain:
        print("{}Type \'card\' to pick a random card or \'coin\' to flip a coin:{}".format(textColours.WARNING, textColours.OKBLUE))

        winnings = ""
        choice = input()

        if choice == 'coin':
            coin1 = coin()
            if coin1 == 1:
                print("\nCoin: tails")
            else:
                print("\nCoin: heads")
        elif choice == 'card':
            pickCard()
        else:
            system("cls")
            print("\n\n{}Invalid Input{}".format(textColours.FAIL, textColours.ENDC))
            break

        choice1 = input("\n{}Would you like to go again? (y/n)\n".format(textColours.WARNING))
        if choice1 == 'n':
            goAgain = False
            system("cls")
            print("{}Thanks for playing".format(textColours.WARNING))
        system("cls")
def Main():
    print("\n{}Welcome to guess the card game!\n".format(textColours.WARNING))

    # TESTS
    # coinOrCard() # play a simple game, all it does is flips a coin or picks a card...
    # print(testColours()) # prints sample text colours
    

    
system("cls")
Main()
# print("{}".format(textColours.ENDC))