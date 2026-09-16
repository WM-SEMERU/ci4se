def parse(self, val):
    s = str(val).lower()
    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        raise ValueError("cannot interpret '{}' as boolean".format(val))