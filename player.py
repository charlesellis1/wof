"""Player classes for Wheel of Fortune game."""

from wordset import WordMunch
from wordset import Dictionary
from utils import *
import random

class Player:
    """Player base class.  Defines initializer and interface.

    >>> from wordset import Dictionary
    >>> p = Player("Fred", Dictionary('assets/lincoln.txt'))
    >>> p.possible_words[2]
    'add'
    """
    def __init__(self, name, dictionary=Dictionary('assets/lincoln.txt')):
        """Inialize the class with a dictionary of words the player can guess from."""
        # BEGIN
        self.name = name
        self.possible_words = dictionary.words()
        # END

    def guess(self, board):
        """Guesses a character and returns it."""
        return None

    def pick_word(self):
        """Return a word that is to be guessed."""
        return None

class DummyPlayer(Player):
    """Simple deterministic player for testing."""

    def __init__(self, name):
        self.name = name
        self.calls = -1

    def guess(self, board):
        """Return the guesses [c,f,e,o,r,s]."""
        self.calls += 1
        return "cfeors"[self.calls]

    def pick_word(self):
        """Sets the dummy word as `score` and returns it."""
        return 'score'


class HumanPlayer(Player):
    """
    HumanPlayer is initialized with a name and implements the player interface
    such that:
    - guess requests a guess from a person, via the input device
    - pick_word requests a secret word and verifies that it is in the dictionary
    """
    def __init__(self, dict=Dictionary('assets/lincoln.txt'), name='Human'):
        """Creates a player with the name and word set"""
        super().__init__(name, dict)

    def guess(self, board):
        """Asks the user to guess a character."""

        print(self.name, ", please enter your next guess.")
        guess = input()
        while (len(guess) != 1) or (guess in board.guesses()):
            print('Please enter a single character not yet guessed')
            guess = input()
        return guess

    def pick_word(self):
        """
        Requests a word from user to use as a secret words.
        Only allows words from the dictionary.
        """
        print(self.name,", pick your secret word.")
        word = input()
        while not word in self.possible_words:
            print(word, " is not in the dictionary. Another:")
            word = input()
        return word

class ComputerPlayer(Player):
    """
    Perform as a player - picking a word or guessing a character
    See the unlock test for examples
    """
    def __init__(self, dict=Dictionary('assets/lincoln.txt'), skill=0, name='Computer'):
        """Creates a player with the name, dict, and skill level"""
        # Replace this when you get to question 5
        super().__init__(name, dict)
        # BEGIN
        self.name = name
        self.dict = dict
        self.skill = skill
        # END

    def guess(self, board):
        """
        Guess a character to play based on the current board
        Uses different strategies based on the players skill level
        Break ties alphabetically, key_of_max does this automatically:)
        """
        # BEGIN
        if self.skill == 0:
            munch = WordMunch(self.possible_words).frequency()
            for i in board.guesses():
                munch.pop(i)
            return key_of_max(munch)

        if self.skill == 1:
            def ffun(word):
                if board.word_len() == len(word):
                    return True
                else:
                    return False
            munch2 = WordMunch(self.possible_words).filter(ffun)
            for i in board.guesses():
                munch2.pop(i, None)
            return key_of_max(munch2)

        if self.skill == 2:
            def ffun2(word):
                if board.word_len() != len(word):
                    return False
                for i in range(len(board.word())):
                    if board.word()[i] != '_':
                        if board.word()[i] != word[i]:
                            return False
                return True

            munch3 = WordMunch(self.possible_words).filter(ffun2)
            for j in board.guesses():
                munch3.pop(j, None)
            return key_of_max(munch3)
        # END

    def pick_word(self):
        """Pick a random word from the dictionary."""
        # BEGIN
        random_word = random.sample(self.possible_words, 1)
        return random_word[0]
        # END
