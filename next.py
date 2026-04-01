from __init__ import cache
from random import choice

_matches = lambda w: [f for f in cache if (f.curr==w and f.next!=None)]

def random(word:str) -> None | str:
        
    matches = _matches(word)

    if len(matches) > 0:
        return choice(matches).next

def probable():

    ''