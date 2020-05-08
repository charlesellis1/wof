from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.
    """
    def __init__(self, picker, guessers):
        # BEGIN
        secret_word = SecretWord(picker.pick_word())
        self.b = Board(secret_word)
        self.guessers = guessers
        self.index = 0
        # END

    def play(self, verbose=True):
        # BEGIN
        self.active = self.guessers[self.index]
        one_guess = self.active.guess(self.b)
        self.b.guess(one_guess)
        if one_guess in self.b.hits:
            self.index += 0
        else:
            if self.index == len(self.guessers) - 1:
                self.index = 0
            else:
                self.index += 1
        if self.b.done() == False:
            return Game.play(self)
        else:
            return self.b


        # END

    def winner(self):
        # BEGIN
        return self.guessers[self.index]
        # END
