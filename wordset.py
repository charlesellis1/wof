from utils import lowercase, key_of_max
import string


#
# WordSet class
#

class WordSet:
    """
    Set of unique words, all in lower case and of positive length.
    """
    def __init__(self, text):
        """
        Form a WordSet from a string of words or collection of words.
        """
        # BEGIN Question 2
        self.text = text
        self.word_set = []
        if type(self.text) is list:
            for word in self.text:
                splitted = word.lower().strip(string.punctuation)
                if splitted not in self.word_set and len(splitted) > 0:
                    self.word_set += [word.lower().strip(string.punctuation)]
        else:
            self.split = self.text.split()
            for word in self.split:
                splitted = word.lower().strip(string.punctuation)
                if splitted not in self.word_set and len(splitted) > 0:
                    self.word_set += [word.lower().strip(string.punctuation)]

        # END Question 2

    def words(self):
        """
        Return sorted list of words in WordSet.

        >>> WordSet("Hi. Hey you. How, the heck, are you?").words()
        ['are', 'heck', 'hey', 'hi', 'how', 'the', 'you']
        """
        # BEGIN Question 2
        return sorted(self.word_set)
        # END Question 2

    def __contains__(self, word):
        # BEGIN Question 2
        if word in self.word_set:
            return True
        else:
            return False
        # END Question 2


#
# Dictionary class
#
class Dictionary(WordSet):
    """
    Construct a dictionary from all the words in a text file.
    Subclass of WordSet with a file based initializer.

    >>> from wordset import Dictionary
    >>> Dictionary('assets/lincoln.txt').words()[55]
    'government'
    """
    def __init__(self, filename):
        with open(filename) as fp:
            text = fp.read()
            WordSet.__init__(self, text)

#
# WordMunch class
#
class WordMunch(WordSet):
    """
    Perform analytics on a set of unique words.

    Subclass of WordSet that provides analytics on the words.
    """
    def filter(self, ffun):
        """Filter set to include only those that satisfy the filter function predicate."""
        # BEGIN
        d = {}
        for word in [word for word in self.word_set if ffun(word)]:
            for char in word:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
        return d
        # END
        # Ffun: Pred func, Takes a word as its argument and returns True or False
        # Need to compare word in word_set to secret_word


    def frequency(self):
        """Return a dictionary of the frequency of each letter in the word set."""
        # BEGIN
        d = {}
        for word in self.word_set:
            for char in word:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1
        return d



        # END
