import copy
import os
import pickle


class Data:
    def __init__(self, path):
        """Imports a data file into a newly created Data object.

        Args:
          path: The path to the data file.
        """
        assert os.path.isfile(path)
        
        f = open(path, 'rb')
        self.words = pickle.load(f)
        self.wconflicts = pickle.load(f)
        self.patterns = pickle.load(f)
        f.close()


    def get_words(self):
        """Get a list of the words.

        Returns:
          A deep copy of the list of words.
        """
        return copy.deepcopy(self.words)
        
        
    def word_conflicts(self, word):
        """Finds the conflicts of a word.

        Args:
          word: The word.

        Returns:
          A set of words conflicting with the word.
        """
        return self.wconflicts[word]

    
    def get_patterns(self):
        """Get a list of the patterns.

        Returns:
          A deep copy of the list of patterns.
        """
        return copy.deepcopy(self.patterns)
