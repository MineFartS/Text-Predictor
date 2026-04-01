from __init__ import cache, Fragment

cache.save([])

punct = ['.', '?']

for s in open('train.txt', encoding="latin-1").readlines():

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

        if len(cache) > 1000:
            exit()
