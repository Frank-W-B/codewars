# You are given the length and width of a 4-sided polygon. The polygon can
# either be a rectangle or a square.  If it is a square, return its area. If it
# is a rectangle, return its perimeter.
#
# Example(Input1, Input2 --> Output):
#
# 6, 10 --> 32
# 3, 3 --> 9
# Note: for the purposes of this kata you will assume that it is a square if
# its length and width are equal, otherwise it is a rectangle.

def area_or_perimeter(length: float, width: float) -> float:
    return length * width if length == width else 2 * (length + width)


if __name__ == '__main__':
    length = 6
    width = 10
    val = area_or_perimeter(length, width)
    print(val)
