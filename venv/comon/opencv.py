from random import choice

class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "hello {name}".format(name=self.name)

def main():
    people = [
        Person('jame'),
        Person('bom')
    ]
    person = choice(people)
    print(person)

if __name__ == '__main__':
    main()
    wrewqerwqerq