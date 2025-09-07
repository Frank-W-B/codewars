# You are given a string containing a sequence of character sequences separate
# by commas. Write a function which returns a new string containing the same
# character sequences except the first and the last ones but this time
# separated by spaces.  If the input string is empty or the removal of the first
# and last items would cause the resulting string to be empty, return an empty
# value (represented as a generic value NULL in the examples below.)

# Examples
# "1,2,3"      =>  "2"
# "1,2,3,4"    =>  "2 3"
# "1,2,3,4,5"  =>  "2 3 4"
#
# ""     =>  Null
# "1"    =>  Null
# "1,2"  =>  Null

def remove_first_and_last_char(string: str) -> str:
    """string contains values separated by commas"""
    vals = string.split(',')
    if len(vals) > 2:
        subset = ' '.join(vals[1:-1])
        return subset
    return None

# best practice solution
def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None


if __name__ == '__main__':
    string = "1,2,3"
    result = remove_first_and_last_char(string)
    print(result)
