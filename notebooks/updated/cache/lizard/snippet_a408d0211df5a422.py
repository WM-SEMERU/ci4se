def random_str(Nchars=6, randstrbase=
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join([randstrbase[random.randint(0, len(randstrbase) - 1)] for
        i in range(Nchars)])