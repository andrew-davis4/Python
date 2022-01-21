import requests
from random import randint
from os import system

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)

wrong = 0

WORDS = response.text.splitlines() # WORDS is a list of words from the url
random_index = randint(0, len(WORDS) - 1)

# print(WORDS)
# print(random_index)
# print(WORDS[random_index])

word = WORDS[random_index]

system("cls")

minlen = int(input("\nEnter a minimum length: "))

maxlen = int(input("\nEnter a maximum length: "))

system("cls")

while(not((len(word) >= minlen) and (len(word) <= maxlen))):
    random_index = randint(0, len(WORDS) - 1)
    word = WORDS[random_index]
    
print(word)
#print(len(word))

def output_hangman(step):
    pass

def output_word():
    for chr in word_list:
        print(chr, end=" ")

#system("cls")
print(word)
#print("---Hangman---\n\n\n")

word_list = []
letters_guessed = ""

for i in range(len(word)):
    word_list.append("_")
    #print("_", end=" ")
#print(underscores)

tries_left = 5

for i in range(len(word)+20):
    if "_" in word_list:
        if wrong < 5:
            system("cls")
            #print("\n---Hangman---\n\n\n")
            output_word()
            #print(word)
            print("\n\nLives remaining:",tries_left)
            print("\nLetters Guessed:", letters_guessed)
            chr_input = input("\nEnter a letter: ")
            letters_guessed += chr_input + " "
            #print("Letters Guessed:", letters_guessed)
            not_match = False
            for j in range(len(word)):
                if chr_input == word[j]:
                    word_list[j] = chr_input
                    not_match = True
            if not not_match:
                wrong += 1
                tries_left -= 1
        else:
            system("cls")
            output_hangman(wrong)
            print("The word was", word)
            exit()
    else:
        system("cls")
        print(word)
        print("\nYou Win!")
        exit()

    

#print("   _____       \n"
#         "  |     |   \n"
#         "  |     |   \n"
#         "  |     |   \n"
#         "  |     O   \n"
#         "  |    /|\  \n"
#         "  |    / \  \n"
#         "__|__       \n")
