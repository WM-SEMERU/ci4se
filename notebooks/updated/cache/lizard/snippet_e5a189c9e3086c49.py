def tokenize(cls, text, mode='c'):
    if mode == 'c':
        return [ch for ch in text]
    else:
        return [w for w in text.split()]