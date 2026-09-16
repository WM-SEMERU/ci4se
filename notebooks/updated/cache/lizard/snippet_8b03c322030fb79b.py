def addSuffixToExtensions(toc):
    new_toc = TOC()
    for inm, fnm, typ in toc:
        if typ in ('EXTENSION', 'DEPENDENCY'):
            binext = os.path.splitext(fnm)[1]
            if not os.path.splitext(inm)[1] == binext:
                inm = inm + binext
        new_toc.append((inm, fnm, typ))
    return new_toc