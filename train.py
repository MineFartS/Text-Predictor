from __init__ import cache, thisd, Word
from philh_myftp_biz.terminal import KIC

cache.save([])

punct = ['.', '?']

KIC.enable()

train_txt = thisd.child('train.txt')

for line in train_txt.open().readlines():

    rline: list[str] = [w.strip() for w in line.lower().split(' ')]

    for x, _ in enumerate(rline):

        word = Word(
            rline = rline,
            index = x
        )

        print(word)

        cache += word

        KIC.check()
