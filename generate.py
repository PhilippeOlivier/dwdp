# This script generates data for a word of length n
# Input: The length of a word
# Output: A pickle file with the words and their conflicts, and
# the patterns and their conflicts

import helper
import itertools
import os
import pickle
import sys
import time

start_time = time.time()

# Size of the words
n = int(sys.argv[1])
filename = str(n) + '.pickle'

# Check if the data already exists
if (os.path.isfile(filename)):
    exit('Data \'%s\' already exists. Aborting data generation.' % filename)
    
# Generate all valid words
words = []
for letters in [word for word in itertools.product('ACGT', repeat=n)]:
    print('Generating words...', end='\r')
    word = ''.join(letters)
    if (helper.constraint_p(n, word)):
        words.append(word)
words = [word for word in words if helper.constraint_rc(n, word, word)]
print('Generating words... Done.')

# Compute conflicts between pairwise words
conflicting_words = [[] for _ in range(len(words))]
for i in range(0, len(words) - 1):
    print('Computing word conflicts... ' +
          str(round(i/len(words)*100)) + '%', end='\r')
    for j in range(i + 1, len(words)):
        if (not helper.constraint_hd(n, words[i], words[j]) or \
            not helper.constraint_rc(n, words[i], words[j])):
            conflicting_words[i].append(j)
            conflicting_words[j].append(i)
print('Computing word conflicts... Done.')

# Generate word patterns
patterns = []
for word in words:
    print('Generating patterns...', end='\r')
    pattern = helper.word_to_pattern(word)
    if not (pattern in patterns):
        patterns.append(pattern)
print('Generating patterns... Done.')

# Compute conflicts between pairwise patterns
conflicting_patterns = [[] for _ in range(len(patterns))]
for i in range(len(words)):
    print('Computing pattern conflicts... ' +
          str(round(i/(len(words)-1)*100)) + '%', end='\r')
    pattern1 = helper.word_to_pattern(words[i])
    index1 = patterns.index(pattern1)
    for j in conflicting_words[i]:
        pattern2 = helper.word_to_pattern(words[j])
        index2 = patterns.index(pattern2)
        if pattern2 not in conflicting_patterns[index1]:
            conflicting_patterns[index1].append(pattern2)
        if pattern1 not in conflicting_patterns[index2]:
            conflicting_patterns[index2].append(pattern1)
print('Computing pattern conflicts... Done.')

# Save data
print('Time elapsed ', time.time() - start_time, 's', sep='')
pickle.dump(words, open(filename, 'wb'))
pickle.dump(conflicting_words, open(filename, 'ab'))
pickle.dump(patterns, open(filename, 'ab'))
pickle.dump(conflicting_patterns, open(filename, 'ab'))
