import random
import re
import csv

with open('words_list.csv') as file:
    read = csv.reader(file)
    items = list(word[0] for word in read)

word = random.choice(items)
secretWord = re.sub('.+?', '_', word)
# secretWordSolution2 = '_'*len(word)

lettersTyped = ""
warningMessage = 'hanged!'
mistake = 0
haveLost = False

while mistake < 7 or secretWord != word:
    print('================= New try :) ===========================')
    inputLetter = (input('Type a letter : '))[0]
    print('')

    if inputLetter in lettersTyped:
        print("{} already typed".format(inputLetter))
        print('')
        print('secret word: ', secretWord)
        print("mistake :", warningMessage[:mistake] or 'no mistakes')
        print('letters already typed: ', '-'.join(lettersTyped))
        print('')
        continue

    letterIndexes = [index for (index, wordLetter) in enumerate(word) if wordLetter == inputLetter]

    if len(letterIndexes) == 0:
        mistake += 1
        if mistake == len(warningMessage):
            print("You loose :( ")
            break

    for letterIndex in letterIndexes:
        secretWord = "".join((secretWord[:letterIndex], inputLetter, secretWord[letterIndex + 1:]))

    if inputLetter not in lettersTyped:
        lettersTyped += inputLetter

    if secretWord == word:
        print('secret word was: ', secretWord)
        print("mistakes made:", mistake or 'no mistakes')
        print('letters typed: ', '-'.join(lettersTyped))
        print("You win :) ")
        break

    print('secret word: ', secretWord)
    print("mistake :", warningMessage[:mistake] or 'no mistakes')
    print('letters already typed: ', '-'.join(lettersTyped))
    print('')


