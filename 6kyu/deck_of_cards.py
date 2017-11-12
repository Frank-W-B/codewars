"""
Build a deck of playing cards by generating 52 strings representing cards. There are no jokers.

Each card string will have the format of:

"ace of hearts"
"ace of spades"
"ace of diamonds"
"ace of clubs"

And will consist of the following ranks:

ace two three four five
six seven eight nine ten
jack queen king

For Python constraints are:

The implementation code should be equal to 1 line of code!
"""
def deck_of_cards():
    suits = ["spades", "diamonds", "hearts", "clubs"]
    values = ["ace", "two", "three", "four", "five",
              "six", "seven", "eight", "nine", "ten",
              "jack", "queen", "king"]
    return [val + " of " + suit for suit in suits for val in values]


if __name__ == '__main__':
    deck = deck_of_cards()
