from random import randint


class Player:
    def __init__(self, nickname):
        self.nick = nickname
        self.lvl = 1
        self.force, self.agility, self.physique = [randint(1, 2) for _ in range(3)]
        self.max_hp, self.hp = self.physique * 10, self.physique * 10
        self.weapon = 'Кулак'
        self.damage = randint(1, 2) * self.force
        self.inventory = {}
        self.kvests = []
        self.active_quest = 1
