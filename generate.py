"""Script to generate data for a word of length n.

Valid words are stored as a list of strings. Conflicts between words are stored
in a dictionary; a key is a word, and its corresponding value is the set of its
conflicting words. Patterns are stored in the same way. This script outputs a
pickle file, which can then be used inside of a Data object.

  Typical usage example:

  # python3 generate.py 8
"""


import helper
import itertools
import os
import pickle
import sys
import time


start_time = time.time()
n = int(sys.argv[1])
rel_path = 'data/' + str(n) + '.pickle'

# Check if the data already exists
if (os.path.isfile(rel_path)):
    exit('Data \'%s\' already exists. Aborting data generation.' % rel_path)
    
# Generate all valid words
words = []
for letters in [word for word in itertools.product('ACGT', repeat=n)]:
    print('Generating words...', end='\r')
    word = ''.join(letters)
    if helper.constraint_p(word) and helper.constraint_rc(word, word):
        words.append(word)
print('Generating words... Done.')

# Compute conflicts between pairwise words
conflicting_words = {word:set() for word in words}
for i in range(0, len(words)-1):
    print('Computing word conflicts... ' +
          str(round(i/len(words)*100)) + '%', end='\r')
    for j in range(i+1, len(words)):
        if (not helper.constraint_hd(words[i], words[j]) or \
            not helper.constraint_rc(words[i], words[j])):
            conflicting_words[words[i]].add(words[j])
            conflicting_words[words[j]].add(words[i])
print('Computing word conflicts... Done.')

# Generate word patterns
patterns = []
for word in words:
    print('Generating patterns...', end='\r')
    pattern = helper.word_to_pattern(word)
    if not (pattern in patterns):
        patterns.append(pattern)
print('Generating patterns... Done.')

# Save data
pickle.dump(words, open(rel_path, 'wb'))
pickle.dump(conflicting_words, open(rel_path, 'ab'))
pickle.dump(patterns, open(rel_path, 'ab'))

print('Time elapsed ', time.time() - start_time, 's', sep='')
