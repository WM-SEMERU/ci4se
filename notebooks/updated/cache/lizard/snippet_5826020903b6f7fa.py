def pip(filename):
    path = join('requirements', filename)
    return [line for line in open(path).readlines() if not line.startswith(
        '-e')]