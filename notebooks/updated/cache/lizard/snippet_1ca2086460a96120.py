def rAsciiLine(ifile):
    _line = ifile.readline().strip()
    while len(_line) == 0:
        _line = ifile.readline().strip()
    return _line