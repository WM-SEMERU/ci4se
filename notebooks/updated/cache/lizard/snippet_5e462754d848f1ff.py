def convert_path(cls, file):
    if isinstance(file, str):
        return file
    elif isinstance(file, list) and all([isinstance(x, str) for x in file]):
        return '/'.join(file)
    else:
        print('Incorrect path specified')
        return -1