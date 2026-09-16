def convertToFree(stream, length_limit=True):
    linestack = []
    for line in stream:
        convline = FortranLine(line, length_limit)
        if convline.is_regular:
            if convline.isContinuation and linestack:
                linestack[0].continueLine()
            for l in linestack:
                yield str(l)
            linestack = []
        linestack.append(convline)
    for l in linestack:
        yield str(l)