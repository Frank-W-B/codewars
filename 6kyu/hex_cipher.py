"""
In order to bamboozle your friends, you decide to encode your communications in hexadecimal, using an ASCII to hexadecimal table. At first, none of them can understand your messages. But quickly enough, one of your cleverer friends uncovers your trick and starts sending messages in hexadecimal himself. To stay one (or shall we say, n) step(s) ahead of your friend, you decide to go one step further : you'll apply the ASCII to hexadecimal conversion more than once.
Your Task

Implement methods encode and decode of class HexCipher, as described above.

Provided to you is a dictionary, TEXT2HEX, mapping ASCII characters to their corresponding hexadecimal code (which will always be 2 digits). For example, TEXT2HEX['a'] evaluates to '61'.

Happy bamboozlin'!
"""

class HexCipher:

    @classmethod
    def encode(cls, s, n):
        # Algorithm to encode the string here
        encoded = s
        for _ in range(n):
            encoded = ''.join(format(ord(c), 'x') for c in encoded)
        return encoded
  
    @classmethod
    def decode(cls, s, n):
        # Algorithm to decode the string here
        decoded = s
        for _ in range(n):
            decoded = ''.join(chr(int(decoded[i:i+2], 16)) 
                              for i in range(0, len(decoded), 2))
        return decoded

"""
class HexCipher_bp:

    HEX2TEXT = {h:c for c,h in TEXT2HEX.items()}

    @classmethod
    def encode(cls, s, n):
        for _ in range(n): 
            s = ''.join(TEXT2HEX[c] for c in s)
        return s
  
    @classmethod
    def decode(cls, s, n):
        for _ in range(n): 
            s = ''.join(HexCipher.HEX2TEXT[s[i:i+2]] for i in range(0,len(s),2))
        return s
"""

from binascii import hexlify, unhexlify
from functools import reduce

class HexCipher_bp2:

    @classmethod
    def transcode(cls, s, n, f): 
        return reduce(lambda x, f: f(x), [f] * n, s)
    
    @classmethod
    def encode(cls, s, n): 
        return cls.transcode(s, n, hexlify)
    
    @classmethod
    def decode(cls, s, n): 
        return cls.transcode(s, n, unhexlify)

if __name__ == '__main__':
    s = "Hey guys"
    n = 3
    print("String: {}".format(s))
    encoded = HexCipher.encode(s, n)
    print("Encoded: {}".format(encoded))
    decoded = HexCipher.decode(encoded, n)
    print("Decoded: {}".format(decoded))

    print("Best practice 2")
    s = "Hey guys"
    n = 3
    print("String: {}".format(s))
    encoded = HexCipher_bp2.encode(s, n)
    print("Encoded: {}".format(encoded))
    decoded = HexCipher_bp2.decode(encoded, n)
    print("Decoded: {}".format(decoded))

