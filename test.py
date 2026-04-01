from __init__ import cache
from random import choice

get_matches = lambda w: [f for f in cache if f.curr==w]

outp = ['The']

print(outp[0], end=' ')

for _ in range(0, 15):

    matches = get_matches(outp[-1])

    if len(matches) > 0:

        match = choice(matches)

        print(match, end=' ')
        
        outp += [match.next]
