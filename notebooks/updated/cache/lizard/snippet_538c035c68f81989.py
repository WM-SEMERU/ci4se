def write(path, data, binary=False):
    mode = 'w'
    if binary:
        mode = 'wb'
    with open(path, mode) as f:
        f.write(data)
    f.close()