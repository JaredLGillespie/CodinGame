# https://www.codingame.com/training/easy/order-of-succession


class Person:
    def __init__(self, name, parent, birth, death, religion, gender):
        self.name = name
        self.parent = parent
        self.birth = birth
        self.death = death
        self.religion = religion
        self.gender = gender

    @classmethod
    def new(cls, text):
        name, parent, birth, death, religion, gender = text.split()
        if parent == '-': parent = None
        if death == '-': death = None
        return cls(name, parent, birth, death, religion, gender)


def person_sort_key(person):
    return (
        0 if person.gender == 'M' else 1,  # Males come first
        person.birth
    )


def traverse(person, relations):
    if person.death is None and person.religion != 'Catholic':
        print(person.name)

    if person.name not in relations: return

    for p in sorted(relations[person.name], key=person_sort_key):
        traverse(p, relations)


def solution():
    num_people = int(input())
    relations = {}
    queen = None

    for i in range(num_people):
        person = Person.new(input())
        if i == 0: queen = person

        if person.parent not in relations:
            relations[person.parent] = []

        relations[person.parent].append(person)

    traverse(queen, relations)


solution()
