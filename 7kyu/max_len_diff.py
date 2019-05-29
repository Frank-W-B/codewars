def min_max_len(lst_s):
    '''min and max length of the strings in a list'''
    len_s = map(lst_s, len)
    return min(len_s), max(len_s)

def mxdiflg(a1, a2):
    min_a1, max_a1 = min_max_len(a1)
    min_a2, max_a2 = min_max_len(a2)

if __name__ == '__main__':
    s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
    s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
