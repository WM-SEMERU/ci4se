def _AddDelta(a, delta):
    if type(delta) == int:
        return a + delta
    if delta == 'EvenOdd':
        if a % 2 == 0:
            return a + 1
        else:
            return a - 1
    if delta == 'OddEven':
        if a % 2 == 1:
            return a + 1
        else:
            return a - 1
    print >> sys.stderr, 'Bad Delta: ', delta
    raise 'Bad Delta'