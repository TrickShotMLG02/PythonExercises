import random


class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        if self.__class__.__name__ == "Fox":
            return f"{self.__class__.__name__} goes {random.choice(self.sound)}"
        else:
            return f"{self.__class__.__name__} goes {self.sound}"


class Dog(Animal):
    def __init__(self):
        super().__init__("woof")


class Cat(Animal):
    def __init__(self):
        super().__init__("meow")


class Bird(Animal):
    def __init__(self):
        super().__init__("tweet")


class Mouse(Animal):
    def __init__(self):
        super().__init__("squeek")


class Cow(Animal):
    def __init__(self):
        super().__init__("moo")


class Frog(Animal):
    def __init__(self):
        super().__init__("croak")


class Seal(Animal):
    def __init__(self):
        super().__init__("ow ow ow")


class Fish(Animal):
    def __init__(self):
        super().__init__("blub")


class Elephant(Animal):
    def __init__(self):
        super().__init__("toot")


class Duck(Animal):
    def __init__(self):
        super().__init__("quack")


class Fox(Animal):
    def __init__(self):
        super().__init__(["Ring-ding-ding-ding-dingeringeding!",
                      "Wa-pa-pa-pa-pa-pa-pow!",
                      "Hatee-hatee-hatee-ho!",
                      "Joff-tchoff-tchoffo-tchoffo-tchoff!",
                      "Jacha-chacha-chacha-chow",
                      "Fraka-kaka-kaka-kaka-kow!"])


def main():
    animals = [Dog(), Cat(), Bird(), Mouse(), Cow(), Frog(), Seal(), Fish(), Elephant(), Duck(), Fox()]
    for animal in animals:
        print(animal.make_sound())


if __name__ == '__main__':
    main()
