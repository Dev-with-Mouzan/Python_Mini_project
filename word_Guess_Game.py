import random
import pyfiglet
banner = pyfiglet.figlet_format("Word Guess")
print(banner)
word_bank=["apple","banana","orange","grapes","dates"]#Change According to your need

word=random.choice(word_bank)
attempts=10
guessedWord = ['_'] * len(word)
while attempts > 0:
   
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' ,attempts)
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
    if attempts==0:
         print('\nYou\'ve run out of attempts! The word was: ' + word)
