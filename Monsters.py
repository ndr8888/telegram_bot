class Monster:
    def __init__(self, name):
        if name == 'weak':
            self.max_hp, self.hp = 10, 10
            self.damage = 1
        else:
            exit(-1)