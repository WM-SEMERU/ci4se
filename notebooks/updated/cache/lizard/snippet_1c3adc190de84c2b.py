def isValidExp(self, exp):
    order = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
        'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']
    l = exp[len(exp) - 1]
    try:
        number = int(exp[0:7])
    except:
        try:
            number = int(exp[0:6])
        except:
            pass
    if l == order[number % 23]:
        return True
    else:
        return False