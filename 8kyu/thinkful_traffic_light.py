"""
You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Create a function update_light() that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to. For example, update_light('green') should return 'yellow'.
"""


def update_light(current):
    options = ["green", "yellow", "red"]
    ind = (options.index(current) + 1) % 3
    return options[ind]


def update_light_bp(current):
    light_transitions ={'green':'yellow','red':'green','yellow':'red'}
    return light_transitions[current]


if __name__ == '__main__':
    current = "green"
    print(update_light(current))

    current = "yellow"
    print(update_light(current))
    
    current = "red"
    print(update_light(current))

