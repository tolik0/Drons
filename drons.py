import random


class CivilDron():
    def __init__(self):
        self.health = 10

    def attack(self, op):
        pass


class ArmoredDron():
    def __init__(self):
        self.health = random.randint(10, 13)

    def attack(self, op):
        op.health -= random.randint(3, 5)


class ArmyDron():
    def __init__(self):
        self.health = random.randint(8, 9)

    def attack(self, op):
        op.health -= random.randint(4, 5)


class MagicDron():
    def __init__(self):
        self.health = random.randint(8, 15)

    def attack(self, op):
        if self.health > op.health:
            op.health -= random.randint(6, 8)
        else:
            self.health -= 1


class Battlefield():

    def play(self, d1, d2):
        if type(d1) == type(d2) == CivilDron:
            print("Draw")
        else:
            print("First drone - {} health {}\nSecond drone - {} health {}"
                  .format(type(d1).__name__, d1.health, type(d2).__name__,
                          d2.health))
            print("Health: 1 - {}, 2 - {}".format(d1.health, d2.health))
            while True:
                d2.attack(d1)
                print("Health: 1 - {}, 2 - {}".format(d1.health, d2.health))
                if d1.health <= 0:
                    print("Second Drone win")
                    break
                d1.attack(d2)
                print("Health: 1 - {}, 2 - {}".format(d1.health, d2.health))
                if d2.health <= 0:
                    print("First Drone win")
                    break


field = Battlefield()
d1 = MagicDron()
d2 = ArmyDron()
field.play(d1, d2)
