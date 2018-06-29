import numpy as np
import pdb

# Codewars best practice? solution
KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/"
MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD)}

def manhattan(*pts): return sum( abs(z2-z1) for z1,z2 in zip(*pts))

def tv_remote_bp(word):
    return len(word) + sum( manhattan(MAP[was], MAP[curr]) for was,curr in zip('a'+word, word))

## all the rest are for my debugging
def map_func(KEYBOARD):
    #pdb.set_trace() 
    map_dict = dict()
    for i, char in enumerate(KEYBOARD):
        key = char
        row = i//8
        col = i%8
        map_dict[key] = (row, col)
    return map_dict

def manhattan_func(*pts):
    #pdb.set_trace()  
    print(*pts)
    sm = 0
    for z1, z2 in zip(*pts):
       diff = (z2 - z1)
       sm += abs(diff)
    return sm

if __name__ == '__main__':
    # check answers for all the test cases 
    wordlist = ["codewars", "does", "your", "solution", "work", "for", "these", "words"]
    correct_presses = [36, 16, 23, 33, 20, 12, 27, 25]

    map_dict = map_func(KEYBOARD)

    word = "does"
    manhattan_lst = []
    pdb.set_trace()
    # investigating tv_remote_bp function
    for was, curr in zip('a'+word, word):
        manhattan_lst.append(manhattan_func(MAP[was], MAP[curr]))

    
    # check that CW best practice solution works
    #for word, correct in zip(wordlist, correct_presses):
    #    assert(tv_remote_bp(word) == correct)



