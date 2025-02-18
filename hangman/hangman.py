import random

from word_list import easy_words

print("Hangman game!\nLet's start!")

#Word for hangman game taken from list in world_list file. using random gen to get word
word = easy_words[random.randint(0, len(easy_words) - 1)]
guess_word = ["_" for x in range(0, len(word))]
words_used = []
counter = 0
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
while True:
    if "_" in guess_word:
        print(word) # TODO for debugging - DELETE LATER
        print(f'Words already guessed: {words_used}')
        letter = input("Guess a letter!\n").lower()
        if letter in alphabet and letter not in words_used:
            if letter in word:
                print(f'Nice guess! Letter {letter} is in the word!')
                index = word.index(letter)
                guess_word[index] = letter
                print(guess_word)
                words_used.append(letter)
            else:
                print(f'Bad guess. Letter {letter} is not in the word!')
                words_used.append(letter)
        else:
            print("Letter already used!" if letter in words_used else "Letter not in alphabet!")
    elif guess_word == word:
        print(f"GOOD JOB! You correctly guessed the word!")
    else:
        break

