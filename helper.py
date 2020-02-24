import copy


def constraint_hd(word1, word2):
    """Checks if two words satisfy the Hamming distance constraint.

    Args:
      word1: The first word.
      word2: The second word.

    Returns:
      A boolean indicating if the constraint is satisfied.
    """
    n = len(word1)
    distance = 0
    for i in (range(n)):
        if (word1[i] != word2[i]):
            distance += 1
    if (distance >= n/2):
        return True
    else:
        return False


def constraint_p(word):
    """Checks if a word satisfies percentage constraint.

    Args:
      word: The word.

    Returns:
      A boolean indicating if the constraint is satisfied.
    """
    n = len(word)
    if (word.count('C') + word.count('G') == n/2):
        return True
    else:
        return False


def constraint_rc(word1, word2):
    """Checks if two words satisfy the reverse complement constraint.

    Args:
      word1: The first word.
      word2: The second word.

    Returns:
      A boolean indicating if the constraint is satisfied.
    """
    reverse1 = word1[::-1]
    reverse2 = word2[::-1]
    wc_comp = lambda s: s.replace('A', 'X').replace('T', 'A').replace('X', 'T') \
        .replace('C', 'X').replace('G', 'C').replace('X', 'G')
    complement1 = wc_comp(word1)
    complement2 = wc_comp(word2)
    if (constraint_hd(reverse1, complement2) and
        constraint_hd(reverse2, complement1)):
        return True
    else:
        return False


def conflict(word1, word2):
    """Checks if two words are conflicting.

    Args:
      word1: The first word.
      word2: The second word.

    Returns:
      A boolean indicating if the words are conflicting.
    """
    return not (constraint_hd(word1, word2) and \
                constraint_p(word1) and \
                constraint_p(word2) and \
                constraint_rc(word1, word2))

    
def word_to_pattern(word):
    """Finds the pattern associated with a word.

    Args:
      word: The word.

    Returns:
      A {x, y} pattern of a {A, C, G, T} word,
      where x is in {A, T} and y is in {C, G}.
    """
    pattern = ''
    for letter in word:
        if (letter in ['A', 'T']):
            pattern = pattern + 'x'
        if (letter in ['C', 'G']):
            pattern = pattern + 'y'
    return pattern


def word_matches_pattern(word, pattern):
    """Checks if a word matches a pattern.

    Args:
      word: The word.
      pattern: The pattern.

    Returns:
      A boolean indicating if the word matches the pattern.
    """
    word_matches = True
    for i in range(len(pattern)):
        if ((word[i] in ['A', 'T'] and pattern[i] != 'x') or \
            (word[i] in ['C', 'G'] and pattern[i] != 'y')):
            word_matches = False
            break
    return word_matches


def is_palindrome(word):
    """Checks if a word is a palindrome.

    Args:
      word: The word.

    Returns:
      A boolean indicating if the word is a palindrome.
    """
    return word == word[::-1]



def viable_words(words, soln):
    """Finds words which can still be added to a solution.

    Args:
      words: The list of all words.
      soln: The words of a solution.

    Returns:
      A list of words which can still be added to a solution.
    """
    candidates = []
    for word in words:
        conflict = False
        for sword in soln:
            if conflict(word, sword):
                conflict = True
                break
        if not conflict:
            candidates.append(word)
    return candidates


def check_solution(words, soln):
    """Validate a solution.

    Checks if there are conflicting words, and if more words can be added
    to the solution.

    Args:
      words: The list of all words.
      soln: The words of a solution.
    """
    for i in range(len(soln) - 1):
        for j in range(i + 1, len(soln)):
            assert (constraint_hd(soln[i], soln[j]) and \
                    constraint_rc(soln[i], soln[j]))
    assert len(viable_words(n, words, soln)) == 0


def word_transformations(word):
    """Finds all the transformations of a base word.

    Args:
      word: The base word.

    Returns:
      A list containing the base word and all its transformations.
    """
    transformations = [word]
    
    tr_at = lambda s: s.replace('A', 'X').replace('T', 'A').replace('X', 'T')
    tr_cg = lambda s: s.replace('C', 'X').replace('G', 'C').replace('X', 'G')
    tr_acgt = lambda s: s.replace('C', 'X').replace('A', 'C').replace('X', 'A') \
        .replace('G', 'X').replace('T', 'G').replace('X', 'T')
    tr_rev = lambda s: s[::-1]
    tr_hs = lambda s: word[4:]+word[:4]
    
    for func in [tr_at, tr_cg, tr_acgt, tr_rev, tr_hs]:
        for word in copy.deepcopy(transformations):
            transformations.append(func(word))
        
    return list(set(transformations))
