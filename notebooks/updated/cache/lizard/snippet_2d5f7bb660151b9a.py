def translate(otp, to=MODHEX):
    if PY3:
        if isinstance(otp, bytes):
            raise ValueError('otp must be unicode')
        if isinstance(to, bytes):
            raise ValueError('to must be unicode')
    else:
        if not isinstance(otp, unicode):
            raise ValueError('otp must be unicode')
        if not isinstance(to, unicode):
            raise ValueError('to must be unicode')
    possible = (set(index[c]) for c in set(otp))
    possible = reduce(lambda a, b: a.intersection(b), possible)
    translated = set()
    for i in possible:
        a = alphabets[i]
        translation = dict(zip((ord(c) for c in a), to))
        translated.add(otp.translate(translation))
    return translated