import random

word_list = ['Grape', 'Lychee', 'Watermelon', 'Mango', 'Apple']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Enter a single letter: ")
               
if len(guess) == 1 and guess.isalpha():
    # Do something
    print("Good guess")
else:
    # Do something else
    print('Oops! That is not a valid input.')
