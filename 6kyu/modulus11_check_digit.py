#number = "03653277227720365327722772"


def add_check_digit(number):
    number_srt = list(reversed(number))
    num_digits = len(number_srt)
    multipliers = list(range(2, 8))
    num_multipliers = len(multipliers)
    num_mults = num_digits // num_multipliers
    num_remainder = num_digits % num_multipliers
    mults = []
    for _ in range(num_mults):
        mults.extend(multipliers)
    for i in range(num_remainder):
        mults.append(multipliers[i])
    sum_digits = sum(int(num) * mult for num, mult in zip(number_srt, mults))
    rm = sum_digits % 11
    if rm == 0:
        cd = "0"
    elif rm == 1:
        cd = "X"
    else:
        cd = str(11 - rm)
    return number + cd


# best practice
from itertools import cycle

def add_check_digit(s):
    rem = 11 - sum(int(a) * b for a, b in zip(
        reversed(s), cycle(xrange(2, 8)))) % 11
    return '{}{}'.format(s, {10: 'X', 11: 0}.get(rem, rem))


from itertools import cycle

def add_check_digit(number):
    fact = cycle([2,3,4,5,6,7])
    r = sum( int(c) * next(fact) for c in number[::-1]) % 11
    return number + ('0' if not r else 'X' if r == 1 else str(11-r))

