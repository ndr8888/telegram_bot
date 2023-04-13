from random import randint


class Player:
    def __init__(self, nickname):
        self.lvl = 1
        self.force, self.agility, self.physique = [randint(1, 2) for i in range(3)]
        self.max_hp, self.hp = self.physique * 10, self.physique * 10
        self.weapon = 'Кулак'
        self.damage = randint(1, 3) * (1 + self.force)
        self.nick = nickname
