def top10(rest):
    if rest:
        topn = int(rest)
    else:
        topn = 10
    selection = Karma.store.list(topn)
    res = ' '.join('(%s: %s)' % (', '.join(n), k) for n, k in selection)
    return res