from turtle import pen


class Bird:
    def __init__(self):
        print('Bird created')

    def whoIAm(self):
        print('I am a Bird')

    def fly(self):
        print('Birds can fly')

    def swim(self):
        print('Birds can swim')


class Owl(Bird):
    def __init__(self):
        print('Owl created')

    def whoIAm(self):
        print('I am an Owl')

    def fly(self):
        print('Owls can fly')

    def swim(self):
        print('Owls can not swim')

    def night_vision(self):
        print('Owls can see at night')


class Penguin(Bird):
    def __init__(self):
        print('Penguin created')

    def whoIAm(self):
        print('I am a Penguin')

    def fly(self):
        print('Penguins can not fly')

    def swim(self):
        print('Penguins can swim')


bird = Bird()
owl = Owl()
peng = Penguin()


def can_it_fly(bird):
    bird.fly()


# Fly Test
can_it_fly(bird)
can_it_fly(owl)
can_it_fly(peng)
