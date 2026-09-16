def almostequal(first, second, places=7, printit=True):
    if first == second:
        return True
    if round(abs(second - first), places) != 0:
        if printit:
            print(round(abs(second - first), places))
            print('notalmost: %s != %s to %i places' % (first, second, places))
        return False
    else:
        return True