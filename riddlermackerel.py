# https://fivethirtyeight.com/features/somethings-fishy-in-the-state-of-the-riddler/
# What is the longest "mackerel"? i.e. the longest word that does not share a letter with only one candidate state.
# Also, what state has the most mackerels? i.e. the most words that it does not share a letter with.

from collections import Counter

def uncommon(str1, str2):

    dict1 = Counter(str1)
    dict2 = Counter(str2)
    commonDict = dict1 & dict2

    if len(commonDict) == 0:  # there are no letters in common
        return True
    else:
        return False

wordvar = open('word.list', 'r')
statevar = open('states.list', 'r')

# Assemble all our words and our states into lists.
# states.list was preprocessed to lowercase and remove spaces (e.g. New York becomes newyork)

all_words = []  # accumulate the words in this list
for line in wordvar:
    words = line.split()  # splits the line on whitespace (blanks, '\n', '\t')
    all_words.extend(words)  # add words in this line to allwords

all_states = []
for line in statevar:
    state = line.split()
    all_states.extend(state)

# let's have a crapload of inefficient variables
mismatch = 0
mismatch_state = ''
longest_length = 0
longest_word = ''
word_count = 0
mackerel_count = 0
mackerel_states = {}

# assemble our dict with a mackerel count of 0 for every state
for state in all_states:
    mackerel_states[state] = 0

# and let's inefficiently compare every single word with every single state, so ~250000 * 50 = 12,500,000 comparisons
# congratulations in advance to the smarter person who does a more efficient approach
for word in all_words:
    # word_count += 1
    # if word_count % 50000 == 0:
    #     print(word_count, "words checked, cool deal")
    for state in all_states:
        if uncommon(word, state):  # there are no letters in common
            mismatch += 1 # the word has mismatched the state
            mismatch_state = state
    if mismatch == 1:  # only one state mismatched our current word
        # increment the mackerel count for the state that mismatched the word
        mackerel_states[mismatch_state] += 1
        if len(word) == longest_length:
            mackerel_count += 1
            print("Tied the longest word with", word, "with length", longest_length,
                  "with no characters in common with", mismatch_state)
        if len(word) > longest_length:
            mackerel_count = 1 # we have a new record, yay team
            longest_length = len(word)
            longest_word = word
            print("The new longest word is", longest_word, "with length", longest_length,
                  "with no characters in common with", mismatch_state)
    mismatch = 0  # and reset our mismatch count.

# What state is our max mackerel count?
max_state = max(mackerel_states, key=mackerel_states.get)
print("The state with the most mismatches is", max_state, "with", mackerel_states.get(max_state))

