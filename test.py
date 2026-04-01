from __init__ import cache
from next import random

outp = []

while True:

    if len(outp) == 0:
        outp += [cache.random().curr]

    m = random(outp[-1])

    if m is None:
        outp = []

    else:

        word = m.replace('.', '')

        print(word, end=' ')
        
        outp += [word]
