'''
Parses a given phrase and returns a phrase key and the hidden form of the
phrase. Phrase can only contain alphabet letters and spaces.
'''
import string

def parse_phrase(phrase):
    #store hidden phrase as a list
    phrase_hidden = []
    #store phrase key as a dictionary of lists containing letter locations
    phrase_key = {}
    
    #reject non-string inputs
    if type(phrase) != str:
        return False
    
    #iterate through given phrase
    for i in range(len(phrase)):
        #convert letter to uppercase
        letter = phrase[i].upper()
        
        #check if letter is valid
        if letter not in (string.ascii_uppercase + ' '):
            return False
        
        #construct hidden phrase
        if letter == ' ':
            phrase_hidden.append(' ')
        else:
            #convert letter to underscore
            phrase_hidden.append('_')
        
        #add letter location to phrase key
        if letter in phrase_key:
            phrase_key[letter].append(i)
        else:
            phrase_key[letter] = [i]
        
    return phrase_hidden, phrase_key
