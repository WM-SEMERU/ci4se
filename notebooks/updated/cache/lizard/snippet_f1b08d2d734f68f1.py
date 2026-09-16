def funname(file):
    if isinstance(file, str):
        files = [file]
    else:
        files = file
    bases = [os.path.basename(f) for f in files]
    names = [os.path.splitext(b)[0] for b in bases]
    if isinstance(file, str):
        return names[0]
    else:
        return names