def long2str(l):
    if type(l) not in (types.IntType, types.LongType):
        raise ValueError('the input must be an integer')
    if l < 0:
        raise ValueError('the input must be greater than 0')
    s = ''
    while l:
        s = s + chr(l & 255)
        l >>= 8
    return s