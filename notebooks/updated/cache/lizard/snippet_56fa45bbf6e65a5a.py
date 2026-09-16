def camelise(text, capital_first=True):

    def camelcase():
        if not capital_first:
            yield str.lower
        while True:
            yield str.capitalize
    if istype(text, 'unicode'):
        text = text.encode('utf8')
    c = camelcase()
    return ''.join(next(c)(x) if x else '_' for x in text.split('_'))