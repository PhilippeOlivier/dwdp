import helper
import pickle
import sys


# Load data
n = int(sys.argv[1])
f = open('data/' + str(n) + '.pickle', 'rb')
words = pickle.load(f)
conflicting_words = pickle.load(f)
patterns = pickle.load(f)
conflicting_patterns = pickle.load(f)
f.close()
