# Returns true if the words satisfy the hamming distance constraint,
# false otherwise
def constraint_hd(n, word1, word2):
    distance = 0
    for i in (range(n)):
        if (word1[i] != word2[i]):
            distance += 1
    if (distance >= n/2):
        return True
    else:
        return False

    
# Returns true if the words satisfy the percentage constraint,
# false otherwise
def constraint_p(n, word):
    if (word.count('C') + word.count('G') == n/2):
        return True
    else:
        return False

    
# Returns true if the words satisfy the reverse complement constraint,
# false otherwise
def constraint_rc(n, word1, word2):
    reverse1 = word1[::-1]
    reverse2 = word2[::-1]
    wc_comp = lambda s: s.replace('A', 'X').replace('T', 'A').replace('X', 'T')\
        .replace('C', 'X').replace('G', 'C').replace('X', 'G')
    complement1 = wc_comp(word1)
    complement2 = wc_comp(word2)
    if (constraint_hd(n, reverse1, complement2) and
        constraint_hd(n, reverse2, complement1)):
        return True
    else:
        return False


# Returns true if the words are conflicting
def conflict(n, word1, word2):
    return not (constraint_hd(n, word1, word2) and \
                constraint_p(n, word1) and \
                constraint_p(n, word2) and \
                constraint_rc(n, word1, word2))

    
# Returns a {x, y} pattern of a {A, C, G, T} word,
# where x is in {A, T} and y is in {C, G}
def word_to_pattern(word):
    pattern = ''
    for letter in word:
        if (letter in ['A', 'T']):
            pattern = pattern + 'x'
        if (letter in ['C', 'G']):
            pattern = pattern + 'y'
    return pattern


# Returns the list of words associated with a pattern
def pattern_to_words(pattern, words):
    pattern_words = []
    for word in words:
        word_is_pattern = True
        for i in range(len(pattern)):
            if ((word[i] in ['A', 'T'] and pattern[i] != 'x') or \
                (word[i] in ['C', 'G'] and pattern[i] != 'y')):
                word_is_pattern = False
                break
        if word_is_pattern:
            pattern_words.append(word)
    return pattern_words


# Returns true if the word is a palindrome, false otherwise
def is_palindrome(word):
    return word == word[::-1]


# Returns a list of words that can still be added to a solution
def viable_words(n, words, sol_words):
    candidates = []
    for word in words:
        compatibility = 0
        for sol_word in sol_words:
            if not conflict(n, word, sol_word):
                compatibility += 1
        if (compatibility == len(sol_words)):
            candidates.append(word)
    return candidates


# Validate a solution by checking (1) if there are conflicting words,
# and (2) if more words can be added to the solution
def check_solution(n, words, sol_words):
    for i in range(len(sol_words) - 1):
        for j in range(i + 1, len(sol_words)):
            assert (constraint_hd(n, sol_words[i], sol_words[j]) and \
                    constraint_rc(n, sol_words[i], sol_words[j]))
    assert len(viable_words(n, words, sol_words)) == 0

