'''
Hangman
Author: Jeff Wen
'''
from parse_phrase import parse_phrase
import random
import string
import re
from draw import draw_stick
import os

class Phrase:
    def __init__(self, phrase, hidden, key):
        self.phrase = phrase
        self.hidden = hidden
        self.key = key
        
        #determine number of unique letters
        if ' ' in self.key:
            self.unique_letters = len(key) - 1
        else:
            self.unique_letters = len(key)
    
    #update hidden list with a correctly guessed letter
    def fill_hidden(self, letter):
        for i in self.key[letter]:
            self.hidden[i] = letter.upper() + ' '
    
    #get current state of hidden phrase
    def get_hidden(self):
        return ' '.join(self.hidden)
    
    #get key
    def get_key(self):
        return self.key
    
    #get phrase
    def get_phrase(self):
        return self.phrase
    
    #get number of unique letters
    def get_unique_letters(self):
        return self.unique_letters

class Game:
    def __init__(self, phrase_list):
        self.score = 0
        self.phrase_list = phrase_list
        self.number_of_phrases = len(phrase_list)
        #generate random order of phrases to be played
        random.shuffle(self.phrase_list)
        #start next phrase
        self.get_next_phrase()    
    
    #get new phrase for game by popping from phrase list and reset guess set
    def get_next_phrase(self):
        self.current_phrase = self.phrase_list.pop()
        self.guess_set = set()
        #allowed 6 incorrect guesses before man is hanged per phrase
        self.guesses_remaining = 6
        #track number of correct guesses to determine if solved
        self.correct_guesses = 0
        #empty list of bad guesses initially
        self.bad_guesses = []
    
    #display current state of the game
    def display(self, valid = True):
        #format for valid guesses needs blank lines at top
        if valid == True:
            print('\n')
        print(self.current_phrase.get_hidden())
        print('\nGuesses Remaining: %s' % self.guesses_remaining)
        print('Bad Guesses: %s' % self.show_bad_guesses())
        print('Score: %s' % self.score)
        draw_stick(self.guesses_remaining)
    
    #check if guess is valid
    def is_guess_valid(self, guess):
        if guess in self.guess_set:
            print('Letter has already been guessed\n')
        elif guess not in string.ascii_uppercase:
            print('Must guess a letter\n')
        elif guess == '':
            print('Cannot guess nothing\n')
        else:
            #add valid guess to guess set
            self.guess_set.add(guess)
            return True
        return False
    
    #check if guess is correct
    def check_guess(self, guess):
        if guess in self.current_phrase.get_key():
            self.correct_guesses += 1
            self.current_phrase.fill_hidden(guess)
        else:
            #reduce number of guesses remaining if incorrect
            self.guesses_remaining -= 1
            self.bad_guesses.append(guess)

    #show incorrect letters guessed
    def show_bad_guesses(self):
        return ' '.join(self.bad_guesses)
    
    #check if phrase is solved
    def is_solved(self):
        if self.correct_guesses == self.current_phrase.get_unique_letters():
            self.score += 1
            return True
        else:
            return False
    
    #check if all phrases are solved and game is won
    def is_won(self):
        return self.score == self.number_of_phrases
    
    #get guesses remaining
    def get_guesses_remaining(self):
        return self.guesses_remaining
    
    #get current phrase
    def get_current_phrase(self):
        return self.current_phrase
    
    #get phrase list
    def get_phrase_list(self):
        return self.phrase_list
    
    #get score
    def get_score(self):
        return self.score
        
def main():
    #clear screen
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    #clear screen on start
    clear()
    
    #print welcome message
    print('Welcome to Hangman')
    print('You will have 6 guesses to guess each word')
    input('Press Enter to continue..')
    
    #parse phrases in phrases.txt and store as list of Phrase objects
    phrase_list = []
    with open('phrases.txt', 'r') as f:
        for phrase in re.findall('\'([^\n]+)\'', f.read()):
            phrase_hidden, phrase_key = parse_phrase(phrase)
            phrase_list.append(Phrase(phrase, phrase_hidden, phrase_key))
    
    #initiate game
    game = Game(phrase_list)
    
    #clear screen to start game
    clear()
    
    #loop game session until game ends
    while True:
        #print hidden phrase and guesses remaining
        game.display()
        
        #move to next phrase if current phrase is solved
        if game.is_solved():
            #check if any phrases remaining
            if game.is_won():
                print('All phrases solved! You win!')
                input('Press Enter to exit..')
                break
            else:
                print('Solved!')
                input('Press Enter to move to next phrase..')
                game.get_next_phrase()
                clear()
                continue
        
        #end game if 0 guesses remaining
        if game.guesses_remaining == 0:
            print('Game Over')
            input('Press Enter to exit..')
            break
        
        #loop until player guesses a valid letter
        while True:
            guess = input('Enter guess: ').upper()
            clear()
            if game.is_guess_valid(guess):
                break
            else:
                game.display(False)
                continue
        
        #check if guess is in phrase and update accordingly
        game.check_guess(guess)

if __name__ == '__main__':
    main()
    
