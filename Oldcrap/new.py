from random import randint


class alien:
    def colour(self,color):
        self.color=color
        print(color)
    def attack(self):
        damage=randint(0,9)
        print(damage)

class lizard:
    def attack(self,damage):
        self.damage=damage
        print(damage)

me=alien()
u=lizard()
u.attack(input('whats the attack'))
me.attack()

