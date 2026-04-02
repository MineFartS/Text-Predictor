from __init__ import cache, Word
from random import choice

outp: list[Word] = []

while True:

    if len(outp) == 0:
        _words = cache.read()
    else:
        _words = outp[-1].instances

    _words = [w for w in _words if len(w.next)>0]
    
    if len(_words) == 0:

        outp = []
    
    else:

        word = choice(choice(_words).next)

        print(word.word.replace('.', ''), end=' ')
        
        outp += [word]
