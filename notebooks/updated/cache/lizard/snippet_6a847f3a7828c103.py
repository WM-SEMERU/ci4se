def shuffle(string):
    s = sorted(string)
    random.shuffle(s)
    return ''.join(s)