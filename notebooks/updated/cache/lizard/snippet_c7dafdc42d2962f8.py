def words(fpth):
    from collections import Counter
    words__ = Counter()
    with open(fpth) as fp:
        for line in fp:
            words__.update(line.strip().split(' '))
    return words__