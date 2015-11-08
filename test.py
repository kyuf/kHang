'''
Test cases for hangman functions
'''
import unittest
from parse_phrase import parse_phrase
import hangman
import os

#test case for phrase parser
class TestParsePhrase(unittest.TestCase):
    #phrase parser should return False when fed a non-letter
    def test_improper_input(self):
        self.assertFalse(parse_phrase('!'))
        self.assertFalse(parse_phrase('?'))
        self.assertFalse(parse_phrase(2))
        self.assertFalse(parse_phrase('4'))
    
    #hidden has a _ for each letter
    def test_hidden(self):
        self.assertEqual(get_parsed('test', 'hidden'), '_ _ _ _ ')
        self.assertEqual(get_parsed('test space', 'hidden'), 
                                    '_ _ _ _   _ _ _ _ _ ')
    
    #key is a dictionary of lists containing letter locations
    def test_key(self):
        hidden, key = parse_phrase('test')
        self.assertEqual(get_parsed('test', 'key'),
                                    {'T': [0, 3], 'E': [1], 'S': [2]})

#helper function for TestParsePhrase
def get_parsed(phrase, select):
    hidden, key = parse_phrase(phrase)
    if select == 'hidden':
        #hidden list is converted to string with join
        return ''.join(hidden)
    elif select == 'key':
        return key

#test case for Phrase class
class TestPhraseClass(unittest.TestCase):
    hidden, key = parse_phrase('test')
    phrase = hangman.Phrase('test', hidden, key)
    def test_unique_letters(self):
        self.assertEqual(self.phrase.get_unique_letters(), 3)    

   
if __name__ == '__main__':
    os.system('clear')
    unittest.main(verbosity=2)
