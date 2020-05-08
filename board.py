"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.guessed = []
        self.secret = secret
        self.board = []
        for char in self.secret.word:
            self.board += ['_']
        self.hits = []
        self.misses = []
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.secret)
        # END

    def word(self):
        """Return the current state of guessing the word as a list of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        return self.board
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return self.guessed
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        return self.hits
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        return self.misses
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        self.guessed += [char]
        if char not in str(self.secret.word):
            self.misses += [char]
            return 0
        else:
            indexes = self.secret.match(char)
            self.hits += [char]
            for ind in indexes:
                self.board[ind] = char
            return len(indexes)
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        return False if '_' in self.board else True
        # END

    def display(self):
        print(self.word())
        print("Guessed chars: ", self.guesses())
