def guess_lineno(file):
    offset = file.tell()
    file.seek(0)
    startpos = 0
    lineno = 1
    while True:
        line = file.readline()
        if not line:
            break
        endpos = file.tell()
        if startpos <= offset < endpos:
            break
        lineno += 1
    file.seek(offset)
    return lineno