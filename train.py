from __init__ import cache, Fragment, thisd
from philh_myftp_biz.terminal import KIC

cache.save([])

punct = ['.', '?']

KIC.enable()

train_txt = thisd.child('train.txt')

for s in train_txt.open().readlines():

    words = s.strip().lower().split(' ')

    for x, word in enumerate(words):

        frag = Fragment()

        if words[x-1][-1] not in punct:
            frag.prev = words[x-1]

        frag.curr = word

        if (word[-1] not in punct) and (len(words) > x+1):
            frag.next = words[x+1]
        
        print(frag)

        cache += frag

        KIC.check()
