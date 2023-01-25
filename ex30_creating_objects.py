class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        else:
            return self.name == other.name and self.age == other.age and self.country == other.country

def create(name, age, country):
    return Person(name, age, country)