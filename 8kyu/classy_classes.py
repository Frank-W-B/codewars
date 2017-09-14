#class Person(object):
#    def __init__(self, name, age):
#        self.info="{0}s age is {1}".format(name, age)


# best practice
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return "{0.name}s age is {0.age}".format(self)


if __name__ == '__main__':
    names=["john","matt","alex","cam"]
    ages=[16,25,57,39]
    person_list = []
    for name, age in zip(names, ages):
        person_list.append(Person(name, age))
    outstr = "\n".join([person.info for person in person_list])
    print(outstr)
