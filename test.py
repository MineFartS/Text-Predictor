from __init__ import Next

outp = []

while True:

    if len(outp) == 0:
        m = Next.random()
    else:
        m = Next.random(outp[-1])

    if m is None:
        outp = []

    else:

        word = m.replace('.', '')

        print(word, end=' ')
        
        outp += [word]
