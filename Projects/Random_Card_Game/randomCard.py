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
# thanks = False

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
    return card((rr(13)+1), (rr(4)+1))
def coin():
    return rr(2)+1
def coinOrCard():
    goAgain = True

    while goAgain:
        system("cls")
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
            print("\nCard: ", pickCard())
        else:
            system("cls")
            print("\n\n{}Invalid Input{}".format(textColours.FAIL, textColours.ENDC))
            break
        choice1 = input("\n{}Would you like to go again? (y/n)\n".format(textColours.WARNING))
        if choice1 == 'n':
            goAgain = False
            system("cls")
            print("{}Thanks for playing{}".format(textColours.WARNING, textColours.ENDC))
def mainGame():
    system("cls")

    repeat = True

    print("\n{}Welcome to guess the card game!\n\n".format(textColours.WARNING))
    balance = int(input("{}First start by entering your 'Data Dollar' bank balance: {}".format(textColours.OKGREEN, textColours.WARNING)))
    balance -= 2

    system("cls")

    while(repeat):
        randomCard = pickCard()
        print(randomCard) # Test

        card1 = input("Pick a card any card!: (i.e. Ace of clubs, 3 of diamonds, ...)\n")
        cardChoice = card1.split()

        print(cardChoice) # Test

        # Car attributes:
        cardValue = ""
        cardSuit = ""
        cardColour = ""
        winnings = 0

        if cardChoice[0] == 'Ace' or cardChoice[0] == 'ace':
            cardValue = 'A'
        elif cardChoice[0] == 'Jack' or cardChoice[0] == 'jack':
            cardValue = "J"
        elif cardChoice[0] == 'Queen' or cardChoice[0] == 'queen':
            cardValue = "Q"
        elif cardChoice[0] == 'King' or cardChoice[0] == 'king':
            cardValue = "K"
        else:
            cardValue = cardChoice[0]
        match cardChoice[2]:
            case 'diamonds': 
                cardSuit = "◇"
                cardColour = "R"
            case 'spades':
                cardSuit = "♤"
                cardColour = "B"
            case 'clubs':
                cardSuit = "♧"
                cardColour = "B"
            case 'hearts':
                cardSuit = "♡"
                cardColour = "R"

        card2 = cardValue+cardSuit
        # system("cls")
        # print(card2)
        
        # print(cardValue+cardSuit,"",cardColour)
        # randomCard = pickCard()
        # print("Random card: ", randomCard)

        randomCardSplit = list(randomCard)
        # print(randomCardSplit)
        randomCardValue = randomCardSplit[0]
        randomCardSuit = randomCardSplit[1]
        if randomCardSuit == "♡" or randomCardSuit == "◇":
            randomCardColour = "R"
        else:
            randomCardColour = "B"

        # system("cls")
        print("{}Random card: ".format(textColours.OKBLUE),randomCard, "\nYour card: ",cardValue+cardSuit, "{}\n".format(textColours.WARNING))
        if randomCard == card2:
            print("Wow! You are one lucky player. \n\n{}You win 40${}".format(textColours.OKGREEN, textColours.WARNING))
            winnings = 40
        else:
            if randomCardValue == cardValue:
                winnings = 4
                print("You guessed", cardValue+cardSuit, "which matches with the", randomCardValue,"of", randomCard,"\n\n{}You win $4{}".format(textColours.OKGREEN, textColours.WARNING))
            else:
                if randomCardSuit == cardSuit:
                    winnings = 2
                    print("You guessed", cardValue+cardSuit, "which matches with the", randomCardSuit,"of", randomCard,"\n\n{}You win $2{}".format(textColours.OKGREEN, textColours.WARNING))
                else:
                    if randomCardColour == cardColour:
                        print("You guessed the correct colour only!\n\n{}You win $1{}".format(textColours.OKGREEN, textColours.WARNING))
                        winnings = 1
                    else:
                        print("Unlucky! You guessed nothing correctly.\n\n{}You win 0${}".format(textColours.FAIL, textColours.WARNING))
        
        # system("cls")

        balance += winnings
        print("\n\nYour balance is",balance)
        repeatChoice = input("\n\n{}Would you like to play again? ('y'/'n')\n{}".format(textColours.OKCYAN, textColours.WARNING))
        if repeatChoice == 'n': 
            repeat = False
            print("{}\n\nThanks for playing{}".format(textColours.OKCYAN, textColours.ENDC))
        else: 
            balance -= 2
            system("cls")

# system("cls")
# TESTS
# coinOrCard() # play a simple game, all it does is flips a coin or picks a card...
# print(testColours()) # prints sample text colours

# MAIN GAME
mainGame()
# if thanks is True:
#     print("{}Thanks for playing{}".format(textColours.OKCYAN, textColours.ENDC))

# print("{}".format(textColours.ENDC))