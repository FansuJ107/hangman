import random

''' A class of a Hangman game, where a player has a minimum of 5 guesses to guess a fruit '''
class Hangman:

    ''' init method with word_list and num_lives as parameters '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    ''' The check guess method which checks whether the letter is in the word. If letter is in word, it replaces the '_' in the word_guessed. If not, it reduces the number of lives by 1 '''
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for index in range(len(self.word)):
                if guess == self.word[index]: self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")    

    ''' The ask for input method checks if the user has entered a single letter and whether the user has already made a guess with the letter entered '''
    def ask_for_input(self):
        guess = input("Enter a single letter guess: ")
        if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
             print("You already tried that letter!")
        else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

''' The play game method initialises the game and sets the number of lives. The game finishes when you have 0 number of lives or when you correctly guess the fruit/word. '''     
def play_game(word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                return
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                return

if __name__ == '__main__':
        word_list = ['grape', 'lychee', 'watermelon', 'mango', 'apple']
        play_game(word_list)