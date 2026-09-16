def read_sphinx_environment(pth):
    with open(pth, 'rb') as fo:
        env = pickle.load(fo)
    return env