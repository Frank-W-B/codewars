# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# test cases
# Every rose has its thorn. -> 7
# Fear is the mindkiller. -> 7
# Xyzzy -> 0


def get_count(sentence: str) -> int:
    vowels = set('aeiou')
    sent_no_vowels = ''.join(c for c in sentence.lower() if c not in vowels)
    num_vowels = len(sentence) - len(sent_no_vowels)
    return num_vowels


# best practice (I guess)
def get_count_bp(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


if __name__ == '__main__':
    sentence = "Every rose has its thorn."
    nv = get_count(sentence)
    print(f'{sentence} has {nv} vowels.')

    sentence = "Xyzzy"
    nv = get_count(sentence)
    print(f'{sentence} has {nv} vowels.')
