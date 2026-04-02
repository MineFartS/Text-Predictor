from philh_myftp_biz.terminal import KIC
from philh_myftp_biz.file import temp
from philh_myftp_biz.web import URL
from __init__ import cache, Word

cache.save([])

punct = ['.', '?']

train_txt = temp('train', 'txt', '0')

train_url = URL('https://media.githubusercontent.com/media/MineFartS/Text-Predictor/refs/heads/master/train.txt')

train_url.cache(train_txt)

KIC.enable()

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
