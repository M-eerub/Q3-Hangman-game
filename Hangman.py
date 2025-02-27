#  Hangman Game

import random
words = ['python', 'hangman', 'javascript', 'vscode', 'laptop']

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman game")
print("_ " * len(words))

while attempts > 0:
    guess = input("\n guess the letters: ").lower()
    
    if len(guess) != 1 or not guess .isalpha():
        print("write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("this letter is already guess chose another letter")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("Correct gues!")
    else:
        attempts -= 1 
        print(f"Wrong {attempts} attempts.")
        
        displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print(displayed_word)
        
        if "_" not in displayed_word:
            print(f"Congratulations! the correct word is {word}")
            break 
        else:
            print(f"Game over! the correct word is: {word}")