def getPhoneInfo(numb):
    text = str(numb)
    info = {}
    node = phonetree
    for c in text:
        chld = node[2].get(c)
        if chld is None:
            break
        if chld[1]:
            info = chld[1]
        node = chld
    return info