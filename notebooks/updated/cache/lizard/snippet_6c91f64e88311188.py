def IntGreaterThanOne(n):
    try:
        n = int(n)
    except:
        raise ValueError('%s is not an integer' % n)
    if n <= 1:
        raise ValueError('%d is not > 1' % n)
    else:
        return n