"""
Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-') between each two odd numbers in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
"""
def is_odd(num_char):
    num = int(num_char)
    if num % 2 == 1:
        return True
    return False

def insert_dash(num):
    num = str(num)
    num_with_dash = num[0]
    for i in range(1, len(num)):
        if is_odd(num[i-1]) and is_odd(num[i]):
            num_with_dash += '-'
        num_with_dash += num[i]
    return num_with_dash
        
# Best practice solution
import re

def insert_dash_bp(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))           
                
if __name__ == '__main__':
    num = 454793
    res = insert_dash(num)
    print(res)

    res = insert_dash_bp(num)
    print(res)
