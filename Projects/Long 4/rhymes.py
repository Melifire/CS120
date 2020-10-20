""" File: rhymes.py
    Author: Ben Kruse
    Purpose: Takes in a dictionary of words and their pronunciations
    and uses them in order to find perfect rhymes with a given input string
"""
# takes a given word and converts it to its pronunciation
word_to_pro = {}
# takes the first stress and everything after it and finds other words with the
# same pattern ("tail")
tail_to_words = {}

pro_file_path = input("")
pro_file = open(pro_file_path, 'r')

for line in pro_file:
    split = line.strip().split()
    word = split[0]
    pro = split[1:]
    for i, ph in enumerate(pro):
        # once it finds the first stress
        if ph[-1] == '1':
            # adds the word and the stress index to the pronunciation dict
            word_to_pro[word] = (pro, i)
            # hashes the tail to make it quicker to reference
            tail_hash = hash(''.join(pro[i:]))
            # adds the hash as the key and the word as the value
            # this code will result in all hashes used leading to a list of 
            # one or more word with the same tail
            if tail_hash not in tail_to_words.keys():
                tail_to_words[tail_hash] = [word]
            else:
                tail_to_words[tail_hash] += [word]


while True:
    try:
        input_word = input().strip().upper()
    except:
        break
    if not input_word:
        print('No word given')
    elif ' ' in input_word:
        print('Multiple words entered, please enter only one word at a time.')
    elif input_word in word_to_pro.keys():
        # printed is used to check if we found any rhymes
        printed = False
        print('Rhymes for: {}'.format(input_word))
        input_pro, stress_index = word_to_pro[input_word]
        # hashes the tail so we can compare it to the tails we already hashed
        tail_hash = hash(''.join(input_pro[stress_index:]))
        word_list = tail_to_words[tail_hash]
        # removes any dupicates from the list and puts it in alphabetical order
        word_list = sorted(list(set(word_list)))
        for word in word_list:
            word_pro, word_index = word_to_pro[word]
            # makes sure the words are not subsets of eachother, the same, or
            # share a common phoneme before the stress
            if (word_index != 0 and stress_index != 0 and 
                input_word != word and 
                input_pro[stress_index-1] != word_pro[word_index-1]):
                print(' ', word.upper())
                printed = True
        if not printed:
            print('  -- none found --')
    # words that cannot be found in the dictionary are stated as 
    # having no rhymes
    else:
        print('Rhymes for: {}\n  -- none found --'.format(input_word))
    print()
            


