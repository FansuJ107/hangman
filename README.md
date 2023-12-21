# Hangman

# Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. Main learning points are being able to use basic Python coding to create the Hagman game as well as using Github as a repository.

# Installation details
In order to play the game, you will need Python installed. Then:
1. Clone the repository to your local machine using https://github.com/FansuJ107
2. Navigate to the projwct directory cd-hangman-game
3. Run the game by executing the script milestone_5.py

# Usage
The game will display a word in which the characters and word length are hidden. You will enter a single character and press Enter in oder to find the hidden word. If the character you enter is correct, it will show up in its position(s). You will have 5 lives and if you have 5 incorrect guesses happen, the game is over. The game is currently loaded with five fruits in the milestone_5.py file but it can be changed to whatever words you want.

# Game Logic

## Hangman class: Attributes
A Hangman class has been created with five attributes

num_lives: Number of lives for user
word_list: List of words the computer will randomly choose from
word: Word chosen by computer from word_list
word_guessed: Includes the letters of the word guessed correctly by the user so far
num_letters which is the number of unique leters in the word
list_of_guesses: Records all letter guesses made by user so far

## Hangman class: Methods
The Hangman class also has two methods. Both methods also update value of some attributes once run

ask_for_input: This asks the user for input (their guess of the letter). It validates the input.
check_guess: This checks whether the letter is part of the word

# File Structure
The hangman file is composed of milestone files for each step of the project. To play the game, only milestone_5.py is needed.

# License
MIT License

Copyright (c) [2023] [Fansu Janneh]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
