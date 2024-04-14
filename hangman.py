# A little game - hangman by YouTube tutorial
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Ensure all words are in uppercase

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, "lives left and you have used these letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', " ".join(word_list))

        user_input = input('Guess a letter: ').upper()
        if user_input.isalpha():  # Check if input is alphabetic
            user_letter = user_input
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives -= 1
                    print('Letter is not in word')
            elif user_letter in used_letters:
                print("You have already used that character. Please try again.")
            else:
                print('Invalid character. Please try again')
        else:
            print('Invalid input. Please enter an alphabetic character.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!!')

hangman()