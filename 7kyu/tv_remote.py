## here is my solution (not needing to submit to codewars)
import string
import numpy as np

def make_keypad():
    ''' Makes a 5 x 8 keypad for the remote '''
    letters = string.ascii_lowercase[:-1] # not including z
    chars = [letter for letter in letters]
    letmat = np.reshape(chars, (5,5))
    numpad = '123456789.@0z_/'
    chars = [num for num in numpad]
    nummat = np.reshape(chars, (5,3))
    return np.hstack((letmat, nummat))

def key_locations(keypad):
    ''' For a keypad numpy array, returns a dictionary
        where the key is the letter/char of the key
        and the value is a tuple (row, column)
    '''
    nrows = keypad.shape[0]
    ncols = keypad.shape[1]
    return {keypad[r,c]: (r,c) for r in range(nrows) for c in range(ncols)}


def distance_between_keys(loc1, loc2):
    ''' Returns the manhattan distance between two key locations.
        The locations are a tuple: (row, column).
    '''
    return abs(loc2[0] - loc1[0]) + abs(loc2[1] - loc1[1]) + 1 

def key_presses(word, keydict):
    ''' Given the string word and a dictionary relating a character
        to its location on the keypad, letter-by-letter determine the 
        number of key presses required to key in the whole word
    '''
    dist = 0 
    prev_char = 'a' # previous character
    for char in word:
        dist += distance_between_keys(keydict[prev_char], keydict[char])
        prev_char = char
    return dist

# my Codewars tv_remote function
import numpy as np
import string

letters = [char for char in string.ascii_lowercase[:-1]]
lettermat = np.reshape(letters, (5,5))
numpad = [char for char in '123456789.@0z_/']
numpadmat = np.reshape(numpad, (5,3))
keypad = np.hstack((lettermat, numpadmat))
nrows = keypad.shape[0]
ncols = keypad.shape[1]
keydict = {keypad[r,c]: (r,c) for r in range(nrows) for c in range(ncols)}


# Codewars best practice? solution
KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/"
MAP      = {c: (i//8, i%8) for i,c in enumerate(KEYBOARD)}

def manhattan(*pts): return sum( abs(z2-z1) for z1,z2 in zip(*pts))

def tv_remote_bp(word):
    return len(word) + sum( manhattan(MAP[was], MAP[curr]) for was,curr in zip('a'+word, word))




def tv_remote(word):
    ''' Given the string word and a dictionary relating a character
        to its location on the keypad, letter-by-letter determine the 
        number of key presses required to key in the whole word
    '''
    dist = 0 
    prev_char = 'a' # previous character
    for char in word:
        presses_leftright = abs(keydict[prev_char][1] - keydict[char][1])
        presses_updown = abs(keydict[prev_char][0] - keydict[char][0])
        dist += presses_leftright + presses_updown + 1
        prev_char = char
    return dist

if __name__ == '__main__':
    keypad = make_keypad()
    keydict = key_locations(keypad)
    # check answers for all the test cases 
    wordlist = ["codewars", "does", "your", "solution", "work", "for", "these", "words"]
    correct_presses = [36, 16, 23, 33, 20, 12, 27, 25]
    print("Key presses on the remote:") 
    for word, correct in zip(wordlist, correct_presses):
        numpresses = key_presses(word, keydict)
        print("{0:<8s}  correct/calculated: {1}/{2}".format(word, 
                                                            correct,
                                                            numpresses))
    
    # check that tv_remote solution for CW works the same as the code using my functions
    for word, correct in zip(wordlist, correct_presses):
        assert(tv_remote(word) == correct)

    # check that CW best practice solution works
    for word, correct in zip(wordlist, correct_presses):
        assert(tv_remote_bp(word) == correct)



