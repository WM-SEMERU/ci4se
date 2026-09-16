def chhome(name, home, persist=False, root=None):
    return _chattrib(name, 'home', home, '-d', persist=persist, root=root)