def lines(fp):
    if fp.fileno() == sys.stdin.fileno():
        close = True
        try:
            fp = open(fp.fileno(), mode='r', buffering=BUF_LINEBUFFERED,
                errors='replace')
            decode = False
        except TypeError:
            fp = os.fdopen(fp.fileno(), 'rU', BUF_LINEBUFFERED)
            decode = True
    else:
        close = False
        try:
            decode = fp.encoding != UTF8
        except AttributeError:
            decode = True
    try:
        while 1:
            l = fp.readline()
            if l:
                if decode:
                    l = l.decode(UTF8, 'replace')
                yield l
            else:
                break
    finally:
        if close:
            fp.close()