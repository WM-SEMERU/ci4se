def should_we_load(kls):
    if kls.__name__.endswith('AbstractCheck'):
        return False
    if not kls.__name__.endswith('Check'):
        return False
    mro = kls.__mro__
    for m in mro:
        if m.__name__ == 'AbstractCheck':
            return True
    return False