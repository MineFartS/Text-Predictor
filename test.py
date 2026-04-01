from next import random

outp = ['the']

print(outp[0], end=' ')

for _ in range(0, 15):

    m = random(outp[-1])

    if m is None:
        break

    word = m.replace('.', '')

    print(word, end=' ')
    
    outp += [word]
