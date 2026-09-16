def random_jpath(depth=3):
    chunks = []
    while depth > 0:
        length = random.randint(5, 15)
        ident = ''.join(random.choice(string.ascii_uppercase + string.
            ascii_lowercase) for _ in range(length))
        if random.choice((True, False)):
            index = random.randint(0, 10)
            ident = '{:s}[{:d}]'.format(ident, index)
        chunks.append(ident)
        depth -= 1
    return '.'.join(chunks)