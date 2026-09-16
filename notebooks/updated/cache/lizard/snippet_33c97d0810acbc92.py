def cd(path):
    _cdhist.append(pwd())
    path = abspath(path)
    os.chdir(path)
    return path