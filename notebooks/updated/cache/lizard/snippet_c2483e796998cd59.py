def multisplit(s, seps=list(string.punctuation) + list(string.whitespace),
    blank=True):
    r
    seps = str().join(seps)
    return [s2 for s2 in s.translate(str().join([(chr(i) if chr(i) not in
        seps else seps[0]) for i in range(256)])).split(seps[0]) if blank or s2
        ]