def encode_notifications(tokens, notifications):
    fmt = '!BH32sH%ds'
    structify = lambda t, p: struct.pack(fmt % len(p), 0, 32, t, len(p), p)
    binaryify = lambda t: t.decode('hex')
    if type(notifications) is dict and type(tokens) in (str, unicode):
        tokens, notifications = [tokens], [notifications]
    if type(notifications) is list and type(tokens) is list:
        return ''.join(map(lambda y: structify(*y), ((binaryify(t), json.
            dumps(p, separators=(',', ':'), ensure_ascii=False).encode(
            'utf-8')) for t, p in zip(tokens, notifications))))