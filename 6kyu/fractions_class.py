#Something goes Here ...

class Fraction:

    def __init__(self, numerator, denominator):
        gcd = self._greatest_divisor(numerator, denominator)
        self.top = numerator // gcd
        self.bottom = denominator // gcd
    
    def _common_denom(self, other):
        return self.bottom * other.bottom

    def _multiply_num(self, orig_num, orig_denom, common_denom):
        mult = common_denom // orig_denom
        return orig_num * mult

    def _nums_and_denom(self, other):
        bottom = self._common_denom(other)
        num_self = self._multiply_num(self.top, self.bottom, bottom)
        num_other = self._multiply_num(other.top, other.bottom, bottom)
        return num_self, num_other, bottom
    
    def _greatest_divisor(self, num1, num2):
        """ Euclid's algorithm, recursive version """
        if num2 == 0:
           return num1 
        else:
           return self._greatest_divisor(num2, num1 % num2)
 
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __add__(self, other):
        num_self, num_other, bottom = self._nums_and_denom(other)
        top = num_self + num_other
        return Fraction(top, bottom)

    def __sub__(self, other):
        num_self, num_other, bottom = self._nums_and_denom(other)
        top = num_self + num_other
        return Fraction(top, bottom)

    def __repr__(self):
        return "{0}/{1}".format(self.top, self.bottom)

# Best practice
class Fraction2:

    def __init__(self, numerator, denominator):
        g = gcd(numerator, denominator)
        self.top = numerator / g
        self.bottom = denominator /g
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    #The rest goes here
    def __add__(self, other):
        numerator = self.top * other.bottom + self.bottom * other.top;
        denominator = self.bottom * other.bottom;
        return Fraction(numerator, denominator)
    
    def __str__(self):
        return str(self.top) + "/" + str(self.bottom)

def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)
    
    #Happy Coding ;)

if __name__ == '__main__':
    f1 = Fraction(1,2)
    f2 = Fraction(1,4)
    f3 = f1 + f2
    f4 = f1 - f2
    f5 = Fraction(50, 60)
