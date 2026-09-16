def readfile(filename):
    with open(path_expand(filename), 'r') as f:
        content = f.read()
    return content