import requests
from random import randint
from os import system

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
response = requests.get(url)

line = 0

WORDS = response.text.splitlines() # WORDS is a list of words from the url
random_index = randint(0, len(WORDS) - 1)

# print(WORDS)
# print(random_index)
# print(WORDS[random_index])

word = WORDS[random_index]
image = ""

system("cls")

while(not((len(word) >= 5) and (len(word) <= 5))):
    random_index = randint(0, len(WORDS) - 1)
    word = WORDS[random_index]

print(word)

for i in range(len(word)+1):
    for j in range(len(word)):
        image += "_ "
    print(image)
    image = ""

word_to_letters = ["", "", "", "", ""]
input_to_letters = ["", "", "", "", ""]

word_input = input("Please enter a 5 letter word: ")
if word_input == word:
    print("You Win!")

