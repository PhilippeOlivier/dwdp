"""Example of a test.

A test verifies an assumption by means of brute force. This text example checks
the distribution of node cardinalities for words of lengths 2, 4, 6, and 8.

  Typical usage example:

  # python3 test_example.py
"""


# Needed to import the custom modules such as data
import sys
sys.path.append('..')

import collections
import data


def node_card_distr(d):
    """Finds the distribution of node cardinalities for a dataset.

    Args:
      d: The dataset in a Data object.

    Returns:
      The distribution of node cardinalities for the dataset.
    """
    cards = []
    for word in d.get_words():
        cards.append(len(d.word_conflicts(word)))
    return collections.Counter(cards)


print('N=2:', node_card_distr(data.Data('../data/2.pickle')))
print('N=4:', node_card_distr(data.Data('../data/4.pickle')))
print('N=6:', node_card_distr(data.Data('../data/6.pickle')))
print('N=8:', node_card_distr(data.Data('../data/8.pickle')))
