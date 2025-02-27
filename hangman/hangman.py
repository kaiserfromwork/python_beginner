import random

from word_list import easy_words

print("Hangman game!\nLet's start!\n")
# Word for hangman game taken from list in world_list file. using random gen to get word
word = easy_words[random.randint(0, len(easy_words) - 1)]
guessing = ["_" for x in range(0, len(word))]


letters_guessed = []
counter = 0
chances = 10


while True:
    print(f"{'Word: ' + ' '.join(guessing)}")
    if guessing == list(word) or counter >= chances:
        print(f"GOOD JOB! You correctly guessed the word!\n")
        break
    elif "_" in guessing:
        print(f"{('Letters guessed: ' + ', '.join(letters_guessed)) if len(letters_guessed) > 0 else 'Good Luck!'}")
        print(f'You have {chances - counter} guesses left!')
        # print(f'Words already guessed: {letters_guessed if len(letters_guessed) > 0 else 0}')
        letter = input("Guess a letter!\n").lower()
        if letter.isalpha() and len(letter) == 1 and letter not in letters_guessed:
            counter += 1
            if letter in word:
                print(f'Nice guess! Letter {letter} is in the word!\n')
                # replaces all occurrences of the letter
                for index, char in enumerate(word):
                    if char == letter:
                        guessing[index] = letter
                letters_guessed.append(letter)
            else:
                print(f'Bad guess. Letter {letter} is not in the word!\n')
                letters_guessed.append(letter)
        else:
            print("Letter already guessed!\n" if letter in letters_guessed else "Not a valid guess!\n")
    else:
        break
