import random
from socketserver import ThreadingTCPServer

maxWordLength = 5
maxGuesses = 6

words = []

replay = False

def filterWords():
    wordsFile = open("answers.txt", "r")
    for word in wordsFile:
        newWord = word.replace("\n", "")
        if len(newWord) != maxWordLength:
            continue
        words.append(newWord)

    wordsFile.close()

def replayCheck():
    replayCheckString = input("Do you want to play again? (Y/n) ")
    if replayCheckString == "Y" or replayCheckString == "y" or replayCheckString == "":
        replay = True
    else: 
        replay = False
    return replay

def playGame():
    guess = ""

    answer = words[random.randrange(0, len(words))]

    # DEBUG:
    print(answer)

    emoticonString = ""
    
    for guesses in range(maxGuesses):
        guess = input("Guess: ")
        while len(guess) != 5:
            print("That's too short or too long, try again!")
            guess = input("Guess: ")

        while guess not in words:
            print("That's not in my dictionary! Try again!")
            guess = input("Guess: ")

        emoticonString = ""
        correctCount = 0

        i = 0
        for char in guess:
            if char == answer[i]:
                emoticonString += "🟢"
                correctCount += 1
            elif char in answer:
                emoticonString += "🟡"
            elif char not in answer:
                emoticonString += "🔴"
            i += 1
        print(emoticonString)
        

        if correctCount == maxWordLength:
            print("Nice job!")
            break

    else: print("You failed, the word was " + '"' + answer + '"' + ", but you're too ignorant to understand that. ")


filterWords()

while True:
    playGame()
    if replayCheck() == False:
        break