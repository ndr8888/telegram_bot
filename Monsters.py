from random import randint
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
golden = morph.parse('золотая')[0]
coin = morph.parse('монета')[0]


class Monster:
    def __init__(self, name):
        if name == 'weak':
            self.max_hp, self.hp = 10, 10
            self.damage = 1
            # для определения лута
            self.rnd = randint(1, 100)

            # 50% шанс, что выпадет 1-2 золотых монет и больше ничего
            if self.rnd < 50:
                self.golden_coins = randint(1, 2)
                self.drop = {'золотые монеты': self.golden_coins}
            # 48% шанс, что выпадет 1-5 золотых монет
            elif self.rnd <= 98:
                self.golden_coins = randint(1, 5)
                self.drop = {'золотые монеты': self.golden_coins}
            # 2% шанс, что выпадет 1-5 золотых монет + руна 1го уровня
            elif self.rnd > 98:
                self.golden_coins = randint(1, 5)
                self.drop = {'золотые монеты': self.golden_coins, 'руны 1-го уровня': 1}
        else:
            exit(-1)
