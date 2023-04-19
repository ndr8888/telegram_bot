from random import randint
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
word1 = morph.parse('золотая')[0]
word = morph.parse('монета')[0]

for i in range(101):
    print(f'{i} {word1.make_agree_with_number(i).word} {word.make_agree_with_number(i).word}')