def get_initial(s, delimiter=' '):
    initials = (p[0] for p in _pinyin_generator(u(s), format='strip'))
    return delimiter.join(initials)